def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

students = []
dict1 = {}
print('-'* 40)
print('欢迎使用通讯录管理系统V0.1')
print('[0] 退出')
print('[1] 增加学员信息')
print('[2] 删除学员信息')
print('[3] 查询学员信息')
print('-'* 40)
while True:
    user_num = (input('请输入你要进行操作的序号：'))
    if is_number(user_num):
        user_num = int(user_num)
        if user_num == 1:
            dict1 = {}
            dict1['name'] = input('请输入姓名：')
            dict1['age'] = input('请输入年龄：')
            dict1['phone_num'] = input('请输入电话：')
            students.append(dict1)
            print(students)
        elif user_num == 0:
            break
        elif user_num == 2:
            name = input('请输入要删除学员的姓名：')
            for i in students:
                if i['name'] == name:
                    students.remove(i)
                    print(students)
                else:
                    print('您要删除的学员不存在')
        else:
            print('输入错误，请重新输入')
    else:
        print('输入错误，请重新输入')