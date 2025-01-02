"""
for 临时变量 in 可迭代对象:
    处理逻辑

使用range() 计数
range(start,end) 从哪开始,不包括end
只写一个数 就是循环的次数

break和continue 同ts
"""

str = 'hello world'
for i in str:
    print(i)

print('\n')

for i in range(1,6):
    print(i)

for i in range(6):
    print('测试')

sum = 0
for i in range(1,101):
    sum += i
print(f'1-100的和为:{sum}')