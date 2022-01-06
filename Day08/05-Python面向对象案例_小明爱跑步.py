class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.__age = 21
        self.a = 21
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight += 1

name = '小明'
weight = 75
xiaoming = Person(name,weight)
xiaoming.run()
xiaoming.eat()
name1 = 'zbh'
weight1 = 75
zbh = Person(name1,weight1)
print(zbh.weight)
print(xiaoming.weight)

