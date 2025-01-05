import copy

"""
深浅拷贝
浅拷贝 copy模块的copy方法
身拷贝 copy模块的deepcopy方法
"""

l1 = [1,2,3,4]
l2 = copy.copy(l1)

print(f'l1为:{l1}')
print(f'l2为:{l2}')

#查看内存地址
print(f'l1的内存地址为:',id(l1))
print(f'l2的内存地址为:',id(l2))

l1.append(8)
print(f'l1新增8后为:{l1}')
print(f'l2未新增8为:{l2}')


#深拷贝
l3 = [1,2,3,['wgg','xq']]
l4 = copy.deepcopy(l3)
l3.append(6)

print(f'l3添加后为:{l3}')
print(f'l4为:{l4}')



"""
可变对象-变量对应的值可以修改,但是内存地址不会发生改变
1.列表
2.字典
3.集合

不可变对象 白能量对应的值不能被修改,如果修改就会生成一个新的值从而重新分配内存空间
1.数值类型
2.字符串
3.元组
"""

str1 = 'wgg'
print(f'str1的地址为:{id(str1)}')
str1 = 'wgg1'
print(f'str1的地址为:{id(str1)}')