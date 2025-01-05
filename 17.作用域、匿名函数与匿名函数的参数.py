"""
作用域
1.主意局部变量和全局变量
2.global 变量名  修改全局变量
"""

#作用域简单理解
a = 100
def test1():
    print(f'test1中a的值为:{a}')
def test2():
    a = 120  #这里的a其实未改变外部的a
    print(f'test2中a的值为:{a}')

print(f'调用前a的值为:{a}')
test1()
test2()
print(f'函数调用后a的值为:{a}') #这里可能和预期结果不一样，因为函数内部使用的变量会先从内部找，找不到去外面找


# 在函数内部修改全局变量的值使用global关键字
a1 = 100
def test1():
    global a1 #修改全局变量
    a1 = 120 
    global name #声明全局变量
    name = 'wgg'
    global p1,p2,p3 #声明多个
    p1 = 1
    p2 = 2
    p3 = 3
    print(f'test1中a1的值为:{a1}')

print(f'函数调用前a1的值为{a1}')
test1()
print(f'test1调用后a1的值为:{a1}')
print(f'全局变量name为:{name}')

"""
nonlocal -了解就行
用来声明外层的局部变量,只能在嵌套函数中使用,在外部函数先进行声明，内部函数进行nonlocal声明
"""

a2 = 10
def outer():
    a2 = 5
    def inner():
        nonlocal a2 #修改上一级的局部变量
        a2 = 20
        print('inner中的a为:',a2)
    inner()
    print('outer中的值为:',a2)
outer()

"""
匿名函数
lambda 形参:返回值(表达式)
"""

add = lambda a,b:a+b 
print('匿名函数执行为',add(5,4))

#匿名函数 参数形式同正常函数参数

#匿名函数结合三目运算符使用
a3 = 7
b3 = 5
comp = lambda a,b: '正确' if a > b else '错误'
print(comp(a3,b3))

