"""
单例模式
方式1:通过@classmethod
方式2::通过装饰器实现
方式3:通过重写__new__()方法实现
方式4::通过导入模块实现
ps:主要用方式34来做

应用场景
1.回收站对象
2.音乐播放器软件
3.数据库配置等
"""


#方法3实现
class Singleton(object):
    obj = None

    def __new__(cls):
        print('我是__new__方法')
        if(cls.obj == None):
            cls.obj = super().__new__(cls)
        return cls.obj
        

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

#方法4实现
from package1 import single

print(single.single1)
print(single.single1)


"""
魔法方法
1.__doc__: 类的描述信息
2.__module__:当前操作对象所在的模块
3.__class__:对象所在的类
4.__str__(): 对象的描述信息,必须return一个字符串
5.__del__():析构函数
6.__call__():使一个实例对象变为一个可调用对象,就像函数可以调用
callable():判断一个对象是否可调用
调用一个可调用对象，其实就是在调用它的__call__()方法
"""

class Person:
    """猜猜我是用来干啥的啊"""

    def __call__(self):
        print('调用可调用对象')


    def funa(self):
        print(self.__module__)
        print(self.__class__)

    def __str__(self):
        print('我是str方法')


person = Person()
print(Person.__doc__)
person.funa()
person.__str__()
person()
print(callable(person))