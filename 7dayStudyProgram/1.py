name = input("请输入姓名：")
age = input("请输入年龄：")
hobbies = input("请输入爱好（多个用逗号分隔）：")

hobbies_list = hobbies.split(",")

print("\n=====个人信息=====")
print(f"姓名：{name}")
print(f"年龄：{age}")
print("爱好：" + ",".join(hobbies_list))
print("================")