# 通讯录的增加操作方法
def add_student():
    """add_student不需要任何参数，只需按照提示输入信息"""
    dict1 = {}
    dict1['name'] = input('请输入姓名：')
    dict1['age'] = input('请输入年龄：')
    dict1['phone_num'] = input('请输入电话：')
    students.append(dict1)
    print(students)

def del_student()
