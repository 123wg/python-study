"""
继承语法
class 类名(父类):
ps: 继承分单继承和多继承

pass #占位符,代码里类下面不写任何东西,会自动跳过,不会报错
"""

#单继承
class Person:
    def __init__(self):
        print('人初始化')

    def eat(self):
        print('person开始吃饭')

class Girl(Person):
    pass 

class Boy(Person):
    def pia(self):
        print('我会打宝')

girl = Girl()
boy = Boy()
girl.eat()
boy.pia()


"""
方法重写
子类调用父类方法:
1.super().方法名()
2.super(子类名,self).方法名
"""

class Person1(Person):
    def eat(self):
        super().eat() #第一种方式 推荐
        super(Person1,self).eat() #第二种方法
        print('我是person1中的方法')

person1 = Person1()
person1.eat()