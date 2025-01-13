"""
多态
发生在继承关系基础上
"""
class Animal:
    def shout(self):
        # print("动物会叫")
        pass

class Cat(Animal):
    def shout(self):
        print('小猫喵喵喵')

class Dog(Animal):
    def shout(self):
        print('小狗汪汪汪')

cat = Cat()
cat.shout()
dog = Dog()
dog.shout()


"""
静态方法
@staticmethod修饰
可以访问类属性，不能访问实例属性
既可以使用类访问，也可以使用对象访问

类方法
@classmethod装饰器标识
第一个参数必须是类对象 一般以cls作为第一个参数
可以访问类属性，不能访问实例属性

应用场景:
1.方法中需要使用功能到类对象(如访问私有类属性等)，定义类方法
2.类方法一般配合类属性使用
"""

class Person:
    name = 'wgggg' # 类属性
    
    @staticmethod
    def study(name):
        print(f'{name}会学习')
    
    @classmethod
    def sleep(cls):
        print(cls) #cls
        print(cls.name) #访问类属性
        print('人类在睡觉')
        

p1 = Person()
p1.study('小伙')
Person.study('wgg')
Person.sleep()