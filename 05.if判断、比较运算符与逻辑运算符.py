"""
比较运算符
== 判断两个变量值是否相等,相等返回True,否则为False


逻辑运算符,这个和ts相差比较大 注意
and 和
or 或
not 非

三元表达式
value_if_true if condition else value_if_false
"""

a = 2
b = 3
print(a == b)

c = 3
if(a == 2 and c == 3):
    print('a和c都符合')

if(c == 3 or a == 5):
    print('c和a有一个符合')

if(not(a > 5)):
    print('a<=5是对的')

# 三目运算符
dd = "对了" if c < 4 else "错了"
print(dd)