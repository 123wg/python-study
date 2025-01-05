"""
类型转换
int(x) 将x转换成一个整数,只能转化由纯数字组成的字符串
float(x) 将x转换为浮点数
str(x) 将x转化为字符串
eval(str) 计算在字符串中的有效表达式,并返回一个对象
tuple(s) 将可迭代对象s转化为一个元组
list(s) 将可迭代对象s转化为一个列表
chr(x) 将整数转化为字符
"""

#浮点型转成整形
a = 1.2
print(f'a转换为整数为,{int(a)}')

#字符串转整形
a1 = '123'
a2 = '1.25'
print(f'a1转换成整数为{int(a1)}')
print(f'a2转化为整数为{float(a2)}')

#eval使用
print(int(eval('10-5')))

#str使用 任何类型都行
a3 = [1,2,3]
print(f'a3转化为字符串为:{str(a3)}')

a4 = (1,2,4)
print(f'a4转化为字符串为:{str(a4)}')

a5 = {'name':'wgg','age':30}
print(f'a5转化为字符串为:{str(a5)}')


#tuple使用
print(tuple([1,2,3]))
print(tuple({'name':'wgg','age':30}))

#list使用
str1 = 'wggert'
print(f'str1使用list转化为:{list(str1)}')
print(list({'name':'wgg','age':30}.values())) #字典转化为列表只取了键名
print(f'集合转列表{list({1,2,3,1})}')