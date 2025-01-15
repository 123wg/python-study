from collections.abc import Iterable,Iterator
name2 = 'wgg'
print(isinstance(name2,Iterable))
print(isinstance(name2,Iterator))

name2 = iter(name2)
print(isinstance(name2,Iterable))
print(isinstance(name2,Iterator))

"""
迭代器协议
对象必须提供一个next方法，执行该方法要么返回下一项，要么引发StopIteration异常,终止迭代

自定义迭代器类
1.有__iter__()和__next__()方法

"""

class Test(object):
    def __init__(self):
        self.num = 1
    
    def funa(self):
        print(self.num)
        self.num += 1

te = Test()
for i in range(5):
    te.funa()

class MyIterator(object):
    def __init__(self):
        self.num = 0
    
    def __iter__(self): #返回的是当前迭代器类的实例对象
        return self

    def __next__(self):
        self.num += 1
        if(self.num > 10):
            raise StopIteration
        return self.num

mi = MyIterator()
print(mi)
for i in mi:
    print(i)