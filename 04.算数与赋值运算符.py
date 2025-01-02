"""
// 取整除,不管四舍五入
使用/运算符,结果一定是浮点数
"""

a = 1/1
print(type(a))

b = 9//2
print(b)
print(type(b))

"""
input输入函数
input(prompt) prompt是提示,会在控制台中显示
"""

name = input('请输入姓名')
print(f'你的名称为:{name}')


"""
转义字符
\t 制表符 通常表示四个字符
\n 换行符
\r 回车 将当前位置移到本行开头
\\ 反斜杠
"""