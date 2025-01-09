#标准版装饰器
def send():
    print('打印日志')

def outer(fn):
    def inner():
        print('登录')
        fn()
    return inner

ot = outer(send)
ot()


#语法糖
"""
@装饰器名称
"""

def outer(fn):
    def inner():
        print('登录=====')
        fn()
    return inner

@outer
def send1():
    print('发送消息=====')

send1()