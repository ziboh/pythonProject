from student import *

class StudentMangerSystem(object):

    def __init__(self):
        self.student_info = []

    def load_student(self):
        try:
            data = open('student.data','r',encoding='utf-8')
        except:
            data = open('student.data','w',encoding='utf-8')
        else:
            while True:
                i = data.readline()
                if i == '':
                    data.close()
                    break
                else:
                    name = i[3:i.find(',')]
                    age = i[i.find('年龄：') +3:i.rfind(',')]
                    mobile = i[i.rfind('：') + 1:-1]
                    info = Students(name,age,mobile)
                    self.student_info.append(info)

    # 判断输入是否为数字
    def is_number(self,s):
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

    @staticmethod
    def show_menu():
        print('-' * 40)
        print('欢迎使用通讯录管理系统V1.0')
        print('[0] 退出')
        print('[1] 增加学员信息')
        print('[2] 删除学员信息')
        print('[3] 查询学员信息')
        print('[4] 修改学员信息')
        print('[5] 遍历所有学员信息')
        print('[6] 保存所有学员信息')
        print('-' * 40)

    def add_student(self):
        name = input('请输入姓名：')
        if self.show_stuendt(name):
            print('您输入的信息已拥有,请勿重复输入')
            return
        age = input('请输入年龄：')
        mobile = input('请输入电话：')
        info = Students(name,age,mobile)
        self.student_info.append(info)

    def del_student(self):
        name = input('请输入您需要删除的学员的姓名：')
        for i in self.student_info:
            if i.name == name:
                self.student_info.remove(i)
                print('删除成功')
                break
        else:
            print('您要删除的学员不存在')

    def modify_student(self):
        name = input('请输入需要修改的学员的姓名：')
        for i in self.student_info:
            if i.name == name:
                while True:
                    print('-' * 40)
                    print('[0] 退出')
                    print('[1] 修改学员姓名')
                    print('[2] 修改学员年龄')
                    print('[3] 修改学员电话')
                    print('-' * 40)
                    user_num = (input('请输入你要进行操作的序号：'))
                    if self.is_number(user_num):
                        user_num = int(user_num)
                        if user_num == 3:
                            i.mobile = input(f'请输入{name}的电话：')
                            break
                        elif user_num == 2:
                            i.age= input(f'请输入{name}的年龄：')
                            break
                        elif user_num == 1:
                            i.name = input(f'请输入修改后的姓名：')
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

    def show_stuendt(self,name):
        for i in self.student_info:
            if i.name == name:
                print(i)
                return 1
        else:
            return 0

    def all_student(self):
        for i in self.student_info:
            print(i)

    def save_student(self):
        data = open('student.data', 'w', encoding='utf-8')
        for i in self.student_info:
            data = open('student.data','a',encoding='utf-8')
            data.write(f'姓名：{i.name},年龄：{i.age},电话：{i.mobile}\n')
        else:
            print('保存信息成功')
            data.close()

    def run(self):
        self.load_student()
        while True:
            self.show_menu()
            user_num = input('请输入要操作功能的编号：')
            if self.is_number(user_num):
                user_num = int(user_num)
                if user_num == 0:
                    print('感谢您使用通讯录管理系统V1.0')
                    break
                elif user_num == 1:
                    self.add_student()
                elif user_num == 2:
                    self.del_student()
                elif user_num == 3:
                    name = input('请输入需要查询的学员的姓名：')
                    if self.show_stuendt(name):
                        pass
                    else:
                        print('您查询的学员不存在')

                elif user_num == 4:
                    self.modify_student()
                elif user_num == 5:
                    self.all_student()
                elif user_num == 6:
                    self.save_student()
                else:
                    print(f'输入错误，请重新输入')
            else:
                print(f'输入错误，请重新输入')