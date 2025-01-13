class Person:
    name = 'wgg' #类属性

    def __init__(self):
        self.age = 18 #实例属性
    
    def play(self):
        print('play方法访问类属性',Person.name) #访问类属性
        print('play方法访问示例属性',self.age)
    
    @staticmethod
    def introduce():
        print('我是:', Person.name) #静态方法能访问类属性，但是无意义(本身与类无关)
    
    @classmethod
    def introduce2(cls): #cls代表类本身
        print('我是:', cls.name) #类方法访问类属性


p1 = Person()
p1.play()
Person.introduce()
Person.introduce2()

"""
单例模式
__init__():构造函数,调用顺序在__new__() 之后

__new__():object基类提供的内置的静态方法
作用:
1.在内存中为对象分配空间
2.返回对象引用
"""

class Test(object):
    def __init__(self,name):
        print('执行__init__()')
    def __new__(cls,*args,**kwargs): #重写
        print('执行__new__()')
        return super().__new__(cls)

test1 = Test('我是测试名')
print(test1)