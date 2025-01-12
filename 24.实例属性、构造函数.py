class Person:
    type = 'dagongren' #类属性,类和实例都能访问

    def __init__(self,name): #构造函数
        print('执行构造函数')
        self.name = name

    def introduce(self):
        print(self.type)
        print('你好,我的名字叫',self.name)

pers = Person('小伙砸')
pers.introduce()