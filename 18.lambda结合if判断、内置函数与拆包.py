comp = lambda a,b: print('a大于b') if a>b else print('a小于等于b')
comp(8,5)


"""
内置函数
查看所有内置函数
import builtins
大写字母开头一般是内置常量名
小写字母开头是内置函数名

常用的几个
zip() 将可迭代对象作为参数,将对象元素打包
map() 不太好用
reduce() 累积
"""

import builtins
# print(dir(builtins))


print(f"-5的绝对值为",abs(-5))

print(f'3和2的和为',sum({2,3}))

#min
print('7和2的最小值为',min([7,2]))
print('-7和2绝对值的最小值为',min([7,2],key=abs))


#max
print('7和2的最大值为',max([7,2]))

#zip
list1 = [1,2,3]
list2 = ['a','b','c'] ## 个数不一致按照短的返回
print('zip结果:',zip(list1,list2))
for i in zip(list1,list2):
    print(i)
    print(type(i))

#转换成列表
print(list(zip(list1,list2)))


#map
list3 = [1,2,3,4]
mp = map(lambda _:_*5,list3)
print('map处理list3结果:',mp)
print(list(mp))

#reduce
from functools import reduce
"""
reduce(function,sequence) #function-函数,必须是有两个参数的函数 sequence-序列:可迭代对象

"""

list4 = [1,2,3,4]
res = reduce(lambda x,y:x+y,list4)
print(f'reduce结果{list[res]}')


"""
拆包 类似于解构
对于函数职工的多个返回数据，去掉元组或列表或字典，直接获取里面数据的过程
"""

# 一般在获取元组值时使用
tua = (1,2,3,4)
a,b,c,d = tua  #数量必须相等
print('拆包后值为:',a,b,c,d)

a1,*b = tua
print('拆包后值为',a,b)


