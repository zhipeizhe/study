import json
from datetime import datetime
from pathlib import Path
import os

# 获取脚本所在目录的绝对路径
SCRIPT_DIR = Path(__file__).parent.resolve()

# 组合文件路径（自动处理跨平台路径分隔符）
TODO_FILE = os.path.join(SCRIPT_DIR, 'todos.json')

def load_todos():
    """加载待办事项"""
    try:
        with open(TODO_FILE, 'r') as f:
            data = json.load(f)
            return data['todos'], data['next_id']
    except (FileNotFoundError, json.JSONDecodeError):
        return [], 1

def save_todos(todos, next_id):
    """保存待办事项"""
    data = {
        "todos": todos,
        "next_id": next_id
    }
    with open(TODO_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_todo(todos, next_id):
    """添加新待办"""
    title = input("请输入事项标题：")
    due_date = input("请输入截止日期（YYYY-MM-DD）：")
    
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("日期格式错误！")
        return
    
    new_todo = {
        "id": next_id,
        "title": title,
        "due_date": due_date.isoformat(),
        "completed": False
    }
    todos.append(new_todo)
    print(f"已添加：{title}")
    return next_id + 1

def list_todos(todos, show_all=False):
    """查看待办事项"""
    now_date = datetime.now().date()

    print("\n=====待办事项=====")
    for todo in todos:
        due_date = datetime.fromisoformat(todo['due_date']).date()    # 从符合 ISO8601 标准的字符串解析出 datetime 对象
        status = '√' if todo['completed'] else ' '
        days_remaining = (due_date - now_date).days    # 计算距离截止日期的天数

        # 过期判断
        if days_remaining < 0:
            status = "⌛"

        if show_all or not todo["completed"]:
            print(f"{todo['id']}.[{status}]{todo['title']} 截止日期：{due_date}（剩余{days_remaining}天）")

def complete_todo(todos):
    """标记待办事项为完成"""
    try:
        todo_id = int(input("请输入待办事项 ID："))
        for todo in todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                print(f"已完成：{todo['title']}")
                return
            print("未找到该事项")
    except ValueError:
        print("请输入有效的ID")

def delete_todo(todos):
    """删除待办事项"""
    try:
        todo_id = int(input("请输入待办事项 ID："))
        for i, todo in enumerate(todos):
            if todo['id'] == todo_id:
                del todos[i]
                print(f"已删除：{todo['title']}")
                return
            print("未找到该事项")
    except ValueError:
        print("请输入有效的ID")

def check_overdue(todos):
    """检查待办事项是否过期"""
    now_date = datetime.now().date()
    overdue = [ # 筛选出截止日期在今天之前的未完成事项
        todo for todo in todos
        if not todo['completed'] and 
        datetime.fromisoformat(todo['due_date']).date() < now_date
    ]

    if overdue:
        print("\n=====过期待办事项=====")
        for todo in overdue:
            print(f"- {todo['title']}（截止于{todo['due_date']}）")
    else:
        print("\n所有事项都在期限内")

def main():
    # 加载待办事项
    todos, next_id = load_todos()

    while True:
        print("\n待办事项管理器")
        print("1. 添加事项")
        print("2. 查看未完成")
        print("3. 查看全部")
        print("4. 标记完成")
        print("5. 删除事项")
        print("6. 检查过期")
        print("7. 退出")

        choice = input("请输入选项：")

        if choice == '1':
            next_id = add_todo(todos, next_id)
            save_todos(todos, next_id)
        elif choice == '2':
            list_todos(todos)
        elif choice == '3':
            list_todos(todos, show_all=True)
        elif choice == '4':
            complete_todo(todos)    # 标记完成
            save_todos(todos, next_id)
        elif choice == '5':
            delete_todo(todos)
            save_todos(todos, next_id)
        elif choice == '6':
            check_overdue(todos)    # 检查过期
        elif choice == '7':
            break
        else:
            print("无效选项")


if __name__ == '__main__':
    main()