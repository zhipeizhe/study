def celsius_to_fahrenheit(c):
    """摄氏度转华氏度"""
    return c * 9/5 + 32

def fahrenheit_to_celsius():
    """华氏度转摄氏度"""
    return (f - 32) * 5/9

def main():
    while True:
        choice = input("请输入1.摄氏度转华氏度 2.华氏度转摄氏度(按q退出)：")

        if choice == 'q':
            break
        if choice not in ['1', '2']:
            print("输入错误，请重新输入！")
            continue
        
        try:
            temp = float(input("请输入温度值："))
        except ValueError:
            print("请输入有效的数字！")
            continue



        if choice == '1':
            c = float(input("请输入摄氏度："))
            f = celsius_to_fahrenheit(c)
            print(f"华氏度为：{f}")