# 定义一个类
class Person():
    # 属性
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address =address

    def __str__(self):
        print('我被打了')
        return f'姓名:{self.name},年龄:{self.age},地址:{self.address}'

    def __del__(self):
        print('删除完毕')
    # 方法
    def eat(self):
        print('我要少吃东西,需要减肥')
    def drink(self):
        print('我不喝饮料')
    def hello(self):
        print(f'姓名:{self.name},年龄:{self.age},地址:{self.address}')


info = [{'name': '周伯华', 'age': '21', 'phone_num': '18773321296'}, {'name': 'zbh', 'age': '32', 'phone_num': ''}]
students = Person(info,'男','湖南')
# students.hello()
# del students
students.hello()
print(students)
