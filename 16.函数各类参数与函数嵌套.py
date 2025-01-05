"""
参数类型
1.必备参数
2.默认参数
3.可变参数
def func(*args): args是一个元组
4.关键字参数
def func(**args): args是字典
"""

#默认参数
def test(a,b=8):
    return a+b
print(test(2))

#可变参数 可传入多个或不传
def func(*c):
    print(c)
func('海绵宝宝','wgg')

#关键字参数
def funca(**kwargs):
    print(kwargs)
funca(name='wgg',age=30) #传值方式,采用键 = 值的形式

"""
函数嵌套
1.嵌套定义
2.嵌套调用
"""

def study():
    print('晚上在学习')

def course():
    study()
    print('python基础')

course()

def study1():
    print(f'stydy1.晚上在学习')
    def course1():
        print('python基础')
    course1()

study1()