class Students(object):
    def __init__(self,name,age,mobile):
        self.name = name
        self.age =age
        self.mobile = mobile

    def __str__(self):
        return f'姓名：{self.name},年龄：{self.age}.地址：{self.mobile}'
