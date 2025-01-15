"""
可迭代对象 Iterable
str、list、tuple、dict、set

可迭代对象的条件
1.实现了__iter__()方法
2.__iter__()方法返回了迭代器对象

for循环的工作原理
1.先通过__iter__()方法获取可迭代对象的迭代器
2.对获取到的迭代器不断调用__next__()方法获取下一个值并将其赋值给临时变量i


判断一个对象是否是已知的数据类型
isinstance(object,type)
"""

from collections.abc import Iterable
print(isinstance(True,(bool,Iterable)))


"""
迭代器Iterator
是一个可以记住遍历位置的对象，在上次停留的位置继续去做一些事情

取完元素后,再使用__next__()会引发StopIteration异常

步骤
1.iter()调用对象的__iter__()方法，并把__iter__()方法的返回结果作为自己的返回值
2.next() 调用对象的__next__()方法,一个个取元素,所有元素取完了，引发StopIteration异常
"""

li = [1,2,3,4,5]

iter1 = iter(li)
print(iter1.__next__())
print(iter1.__next__())

iter2 = li.__iter__()
print(iter2.__next__())
print(iter2.__next__())