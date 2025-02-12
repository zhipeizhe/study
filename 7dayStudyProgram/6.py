def basic_file_operation(Exception):
    """基础文件操作"""
    try:
        with open("data.txt" , "r") as f:
            content = f.read()

        with open("data.txt" , "w") as f:
            f.write("Hello, world!")

    except FileNotFoundError as e:
        print(f"File not found.{str(e)}")
    except PermissionError as e:
        print(f"Permission denied.{str(e)}")
    except Exception as e:
        print(f"Error:{str(e)}")

    finally:
        print("清理完毕。")


# 添加输入验证与自定义异常
class InvalidFileError(Exception):
    """自定义文件异常"""
    def __init__(self, fileName):
        super().__init__(f"非法文件：{fileName}")
        self.fileName = fileName

def validata_file_name(fileName):
    """验证文件名"""
    if not fileName.endswith(".txt"):
        raise InvalidFileError(fileName)
    if '/' or '\\' in fileName:
        raise InvalidFileError(fileName)
    return True

def log_error(error):
    """示例日志记录函数（需根据实际需求实现）"""
    import logging
    logging.basicConfig(filename='security.log', level=logging.ERROR)
    logging.error(str(error))

def safe_file_write():
    """安全的文件写入"""
    try:
        fileName = input("请输入文件名：")
        validata_file_name(fileName)
        with open(fileName, "w") as f:
            f.write("Hello, world!")

    except InvalidFileError as e:
        print(f"非法文件：{str(e)}")
        log_error(e)  # 记录安全事件
    except ValueError as e:
        print(f"输入错误：{str(e)}")
    except Exception as e:
        print(f"错误：{str(e)}")


# 添加数据完整性校验
import hashlib
import json

def checksum(data):
    """计算文件的校验和"""
    return hashlib.sha256(data.encode()).hexdigest()

def secure_save():
    """安全的文件保存"""
    filename = "important.dat"
    data = "机密数据"

    # 生成校验和
    data_with_checksum = {
        "data" : data,
        "checksum" : checksum(data),
    }

    try:
        with open(filename, "w") as f:
            json.dump(data_with_checksum, f)
    
    except json.JSONDecodeError as e:
        print(f"数据格式错误：{str(e)}")
    except IOError as e:
        print(f"文件操作错误：{str(e)}")

    else:
        print(f"文件保存成功：{filename}")

def secure_load():
    """安全的文件加载"""
    filename = "important.dat"

    try:
        with open(filename, "r") as f:
            loaded = json.load(f)
        
        # 验证校验和
        if loaded['checksum'] != checksum(loaded['data']):
            raise ValueError("数据完整性校验失败")
        
    except (json.JSONDecodeError, KeyError) as e:
        print(f"文件已损坏：{str(e)}")
    except ValueError as e:
        print(f"安全警报：{str(e)}")
    except KeyError as e:
        print(f"文件格式错误：{str(e)}")

# 实现安全删除（带异常处理）
import os
import random

def secoure_delete(path):
    """安全的文件删除"""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"文件{path}不存在")
        
        # 获取文件大小
        size = os.path.getsize(path)

        # 三次复写
        with open(path, "wb") as f:
            for _ in range(3):
                f.seek(0)
                f.write(os.urandom(size))

        # 重名后删除文件
        temp_name = str(random.randint(1,10000))
        os.rename(path, temp_name)
        os.remove(temp_name)

    except PermissionError as e:
        print(f"删除失败，权限不足：{str(e)}")
    except Exception as e:
        print(f"安全删除异常：{str(e)}")
    finally:
        if os.path.exists(path):
            print(f"文件未完全删除：{path}")

# 完整安全文件操作类
from pathliib import Path
import logging

class SecureFileMananger:
    """安全的文件管理类"""
    def __init__(self, work_dir = "secure_data"):
        self.work_dir = Path(work_dir)
        self.setup()
        logging.basicConfig(filename='security.log', level=logging.INFO)

    def setup(self):
        """初始化工作目录"""
        try:
            self.work_dir.mkdir(exist_ok=True, mode=0o700)
        except PermissionError as e:
            print(f"创建工作目录失败，权限不足：{str(e)}")

    def _validate(self, filename):
        """综合验证"""
        path = self.work_dir / filename
        if not path.resolve().parent == self.work_dir.resolve():
            raise InvalidFilenameError("路径遍历攻击检测")
        return path

    def save_file(self, filename, data):
        """保存文件"""
        try:
            path = self._validate(filename)

            # 输入验证
            if not isinstance(filename, str):
                raise TypeError("文件名必须为字符串")
            
            # 备份机制
            if path.exists():
                backup = path.with_suffix(".bak")
                path.rename(backup)

            # 原子写入
            temp_name = self.work_dir / f"{filename}.tmp" # 临时文件名
            try:
                with open(temp_name, "w") as f:
                    f.write(data)
                temp_name.rename(path)
            finally:
                if temp_name.exists():
                    temp_name.unlink()

            logging.info(f"文件保存成功：{filename}")
            
        except (InvalidFilenameError, TypeError) as e:
            logging.warning(f"输入验证失败：{str(e)}")
            raise
        except Exception as e:
            logging.error(f"保存失败：{str(e)}")
            raise
            
    def load_file(self, filename):
        """加载文件"""
        try:
            path = self._validate(filename)

            if not path.exists():
                raise FileNotFoundError
            
            with open(path, "r") as f:
                return f.read()
            
        except FileNotFoundError:
            logging.warning(f"文件不存在：{filename}")
            raise
        except UnicodeDecodeError:
            logging.error("检测到非文本文件")
            raise ValueError("文件格式错误")

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文结束时进行安全检查"""
        if exc_type is not None:
            logging.error(f"操作异常终止：{exc_type.__name__}")
