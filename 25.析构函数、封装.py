"""
析构函数
__del__ 方法
在对象被垃圾回收的时候使用功能的,使用后对象不能继续使用
"""

class A:
    def __del__(self):
        print('实例销毁')
    
a = A()
print('最后一句')

"""
隐藏属性: __开头的属性,子类不会继承
外部访问方法:
1.隐藏属性实际上是将名字修改为 _类名__属性名 
2.实例方法返回
"""

class Person:
    name ='wgg'
    __age = 20  #隐藏属性
    _sex = '男' #私有属性

    def __init__(self):
        print('我是Person的构造函数')

    def introduce(self):
        print('Person的age是',self.__age)

    def __play(self):   #隐藏方法
        print('玩手机')
    
    def _jump(self):
        print('起跳')

person = Person()
person.introduce()
print(person._sex)
person._Person__play()
person._jump()

"""
私有属性: _开头,外部可直接使用,子类可继承
"""