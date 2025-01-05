"""
函数
    def 函数名():
        函数体
    return 函数返回值,返回多个值，会以元祖的形式返回
"""

def login():
    print('这是登录函数')

login()

#函数返回值 默认返回为None
def buy():
    return "一桶水果茶",20

print(buy())

#参数
def add(x,y):
    return x+y
print(f'add的执行结果为:{add(5,6)}')