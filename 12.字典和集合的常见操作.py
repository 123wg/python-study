"""
1.求长度 len
2.keys() 返回包含的所有键名,注意数据类型不是列表
3.values 返回包含的所有值
4.items() 键值对以元组形式返回
"""

dic = {
    'name':'wgg',
    'age':20 
}

print(f"dic的长度为{len(dic)}")

print(f"dic的所有键:{dic.keys()}")

print(f'dic的所有值为:{dic.values()}')

for i in dic.values():
    print(i)


for items in dic.items():
    print(f"返回数据为:{items}")
    print(f'元组中第一个数据为{items[1]}')

"""
集合-两种方式创建
s = {1,2,3} 可以是不同数据类型
s = {} 代表的是空字典,不是几何
s = set()
集合是无序的,可自动去重
"""

s1 = {1,2,3}

print(f's1的类型为:{type(s1)}')

"""
集合的常见操作
add() 添加的是一个整体,一次只能添加一个元素,一次添加多个只能用元组
update() 把传入的元素拆分，一个个放入集合中，可添加列表
"""

s2 = {1,2,3}
print(f's2初始值为:{s2}')
s2.add(5)
print(f's3.add(5)后的值为:{s2}')
s2.add((5,4))


s3 = {1,2,3}
s3.update([2,5,6]) # 加列表
s3.update({2,7,6}) # 加集合
s3.update((9,0)) # 加元组
s3.update({'a':10}) # 加字典 -只添加了键
print(f's3.update添加列表{s3}')


"""
集合的删除
remove(ele) 选择删除的元素，有就删除，没有就报错
pop() 默认删除根据hash排序后的第一个元素
discard(ele) 删除元素,不存在不会报错 
"""

s4 = {1,2,3}
s4.remove(3)
print(f's4删除3后为:{s4}')

s5 = {1,2,3,4,5}
s5.pop()
print(f's5使用po后为:{s5}')


"""
交并差
"""

s6 = {1,2,3}
s7 = {2,3}
print(f's67的交集为:{s6.intersection(s7)}')
print(f's67的并集为:{s6.union(s7)}')
print(f's6的差集为:{s6.difference(s7)}')