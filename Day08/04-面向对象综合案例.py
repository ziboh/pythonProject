class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_info(self):
        if self.score >= 90:
            print(f'{self.name}的成绩为{self.score},优秀')
        elif self.score >= 80:
            print(f'{self.name}的成绩为{self.score},良好')
        elif self.score >= 70:
            print(f'{self.name}的成绩为{self.score},中等')
        elif self.score >= 60:
            print(f'{self.name}的成绩为{self.score},及格')
        elif self.score >= 0:
            print(f'{self.name}的成绩为{self.score},不及格')
        else:
            print('输入错误')

zhou = Student('周伯华',99)
zhou.print_info()