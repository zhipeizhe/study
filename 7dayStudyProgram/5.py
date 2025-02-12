import csv
import os

contacts_file = "contacts.csv"
contacts = []

def add_contact():
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    email = input("请输入邮箱地址：")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("添加成功！")

def show_contacts():
    if not contacts:
        print("联系人列表为空！")
        return
    print("\n===== 联系人列表 =====")
    for contact in contacts:
        print(contact)
    print("======================\n")

def save_to_file():
    if not contacts:
        print("联系人列表为空！")
        return
    with open(contacts_file, "w", newline="", encoding="utf-8") as f:
        wrirter = csv.DictWriter(f, fieldnames=["name", "phone", "email"])  # 将字段写入csv文件
        wrirter.writeheader()
        wrirter.writerows(contacts)  # 将数据写入csv文件
    print("保存成功！")

def load_from_file():
    global contacts
    if not os.path.exists(contacts_file):
        print("文件不存在！")
        return
    try:
        with open(contacts_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            contacts = list(reader)
        print("加载成功！")
    except Exception as e:
        print("加载失败！", e)

def mian():
    while True:
        print("1、添加联系人")
        print("2、显示所有联系人")
        print("3、保存到文件")
        print("4、从文件加载联系人")
        print("5、退出程序")
        choice = input("请选择：")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            load_from_file()
        elif choice == "5":
            exit()
        else:
            print("输入错误，请重新输入！")

if __name__ == "__main__":
    mian()
