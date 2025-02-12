students = []

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

def add_student():
    name = input("请输入学生姓名：")
    grade = input("请输入学生成绩：")
    student = Student(name,grade)
    students.append(student)
    print("学生信息添加成功！")

def delete_student():
    name = input("请输入要删除的学生姓名：")
    for stu in students:
        if stu.name == name:
            students.remove(stu)
            print("学生信息删除成功！")
            return
    print("没有找到该学生信息！")

def query_student():
    name = input("请输入要查询的学生姓名：")
    for stu in students:
        if stu.name == name:
            print(f"姓名：{stu.name},成绩：{stu.grade}")
            return
    print("没有找到该学生信息！")

def modify_student():
    name = input("请输入要修改的学生姓名：")
    for stu in students:
        if stu.name == name:
            new_grade = input("请输入新的学生成绩：")
            stu.grade = new_grade
            print("学生信息修改成功！")
            return
    print("没有找到该学生信息！")

def show_students():
    if not students:
        print("暂无学生信息！")
        return
    print("\n===== 学生信息列表 =====")
    for student in students:
        print(f"姓名：{student.name},成绩：{student.grade}")
    print("=========================\n")

def main():
    while True:
        print("\n===== 学生信息管理系统 =====")
        print("1、添加学生信息")
        print("2、删除学生信息")
        print("3、查询学生信息")
        print("4、修改学生信息")
        print("5、显示学生信息")
        print("6、退出系统")

        choice = input("请输入你的选择：")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            query_student()
        elif choice == '4':
            modify_student()
        elif choice == '5':
            show_students()
        elif choice == '6':
            break
        else:
            print("输入错误，请重新输入！")

if __name__ == '__main__':
    main()
