"""
生成器 generator
一遍循环一遍计算的机制

使用了yield的函数被称为生成器

1.生成器表达式
2.生成器函数
 使用yield关键字的函数，为生成器函数
 yield类似于return，将指定值或者多个值返回给调用者，一次返回一个结果，在每个结果中间，挂起函数，执行next()，再重新从挂起点继续执行
"""


#生成器表达式
gen = (i*5 for i in range(5))
# print(gen)
print(gen.__next__())
print(gen.__next__())


#生成器函数
def yGen():
    print('开始')
    yield 1 #返回1后暂停函数 挂起
    yield 2
    yield 3
ygen = yGen()
print(ygen)
print(ygen.__next__())


def gen2(n):
    li = []
    for i in range(n):
        li.append(i)
        yield li

for i in gen2(5):
    print('gen2值',i)


"""
范围: 可迭代对象 > 迭代器 > 生成器

"""