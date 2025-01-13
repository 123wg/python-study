"""
新式类:不需要多看，python3都是新式类
"""


"""
多继承
不同的父类具有同名方法:谁写在前就调用谁
python内置的属性__mro__可以查看方法搜索顺序
"""
class Father:
    def money(self):
        print('有一百万资产需要被继承')

class Mother(object):
    def appearance(self):
        print('绝世容颜需要被继承')
    
    def money(self):
        print('我有两百万')

class Son(Father,Mother):
    pass

son = Son()
son.money()
son.appearance()

print(Son.__mro__)