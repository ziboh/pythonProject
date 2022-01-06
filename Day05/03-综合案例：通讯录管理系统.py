import os
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

def menu():
    print('-' * 40)
    print('欢迎使用通讯录管理系统V0.1')
    print('[0] 退出')
    print('[1] 增加学员信息')
    print('[2] 删除学员信息')
    print('[3] 查询学员信息')
    print('[4] 修改学员信息')
    print('[5] 遍历所有学员信息')
    print('-' * 40)

def add_info():

    dict1 = {}
    global students
    dict1['name'] = input('请输入姓名：')
    if inquire_info(dict1['name']):
        print('您输入的信息已拥有,请勿重复输入')
        return 0
    dict1['age'] = input('请输入年龄：')
    dict1['phone_num'] = input('请输入电话：')
    students.append(dict1)

def del_info(name):
    global students
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print('删除成功')
            break
    else:
        print('您要删除的学员不存在')

def inquire_info(name):
    for i in students:
        if i['name'] == name:
            age = i['age']
            phone_num =i['phone_num']
            print(f'姓名：{name},年龄：{age},电话：{phone_num}')
            return 1
    else:
        return 0

def modif_info(name):
    for i in students:
        if i['name'] == name:
            while True:
                print('-' * 40)
                print('[0] 退出')
                print('[1] 修改学员姓名')
                print('[3] 修改学员年龄')
                print('[2] 修改学员电话')

                print('-' * 40)
                user_num = (input('请输入你要进行操作的序号：'))
                if is_number(user_num):
                    user_num = int(user_num)
                    if user_num == 3:
                        i['age'] = input(f'请输入{name}的年龄：')
                        break
                    elif user_num == 2:
                        i['phone_num'] = input(f'请输入{name}的年龄：')
                        break
                    elif user_num == 1:
                        i['name'] = input(f'请输入修改后的姓名：')
                        break
                    elif user_num == 0:
                        break
                    else:
                        print('输入错误，请重新输入')
                else:
                    print('输入错误')
                    continue
            break
    else:
        print('您需要修改的信息没有')

def all_info():
    print(students)
    for i in students:
        name = i['name']
        age = i['age']
        phone_num =i['phone_num']
        print(f'姓名：{name},年龄：{age},电话：{phone_num}')

students = []
while True:
    dict1 = {}
    # i = os.system('cls')
    menu()
    user_num = (input('请输入你要进行操作的序号：'))
    if is_number(user_num):
        user_num = int(user_num)
        if user_num == 1:
            add_info()
        elif user_num == 0:
            break
        elif user_num == 2:
            if students == []:
                print('没有可以删除的学员信息，请添加')
            else:
                name = input('请输入要删除学员的姓名：')
                del_info(name)
        elif user_num == 3:
            if students == []:
                print('没有可以查询的学员信息，请添加')
            else:
                name = input('请输入要查询学员的姓名：')
                if not inquire_info(name):
                    print('您查询的信息没有')

        elif user_num == 4:
            if students == []:
                print('没有可以修改的学员信息，请添加信息')
            else:
                name = input('请输入要修改学员的姓名：')
                modif_info(name)
        elif user_num == 5:
            if students == []:
                print('没有可以遍历的学员信息，请添加信息')
            else:
                all_info()
        else:
            print('输入错误，请重新输入')
    else:
        print('输入错误，请重新输入')