"""
1.元组 tuple
    基本格式: 元祖名 (元素1，元素2，元素3)，可以是不同的数据类型
    只有一个元素时,末尾要加上逗号
和列表的区别,只支持查询操作,不支持增删改

使用场景
- 函数的参数和返回值
- 格式化输出后面的()本质上就是一个元组
- 数据不能被修改的时候
"""

tua = (1,2,3,4,5,'wgg',[1,2,3])
print(f"tua的类型为:{type(tua)}")

print(f'tua的第二个值为:{tua[1]}')

print(f"tua的长度为:{len(tua)}")

print(f"tua中3的下标为:{tua.index(3)}")

print(f"tua的切片1-3为:{tua[1:3]}")

tua1 = ('a')
print(f"tua1的类型为{type(tua1)}")

name = 'wgg'
age = 29
print("%s的年龄是:%d",(name,age))

info = (name,age)
print(info)


"""
字典格式-键值对和ts的对象一样
dic = {'name':'wgg','age':18}
"""

dic = {
    'name':'wgg',
    'age':20
}
print(f'dic字典的值为:{dic}')
print(f"dic的类型为:{type(dic)}")

"""
字典的增删改查
1.查看元素
变量名[键名]
变量名.get(键名) 键名不存在返回null
2.修改
update(字典) 类似object.assign
3.添加
4.删除元素
del 字典名 删除整个字典
del 字典[属性名]
clear清空字典
pop 删除键,不存在报错
popitem() 默认删除最后一个键值对
"""

print(f'dic中的name为:{dic['name']}')

print(f"get获取dic的name值为{dic.get('name','不存在返回')}")

dic['age'] = 30
print(f"通过下标修改后为:{dic}")

dic['height'] = 50
print(f'添加height后为:{dic}')

dic1 = {'type':'insert'}
dic.update(dic1)
print(f'dic.update(dic1)后的值为:${dic}')


# 删除字典
# del dic
# print(dic)

# 删除指定键值对,键名不存在报错
del dic['age']
print(f'删除age后为:{dic}')