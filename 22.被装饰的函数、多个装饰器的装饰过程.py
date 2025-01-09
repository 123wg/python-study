#被装饰的函数有参数
def outer(fn):
    def inner(name):
        print(f'用户名{name},登录=====')
        fn(name)
    return inner

@outer
def send1(name):
    print('发送消息=====')

send1('wgg')

#被装饰的参数有可变参数*args,**kwargs



#多个装饰器
def decol(fn):
    def inner():
        return '第一个装饰器'+fn()+'结束1'
    return inner

def decol1(fn):
    def inner():
        return '第二个装饰器'+fn()+'结束2'
    return inner

#多个装饰器的装饰过程 离函数最近的先装饰,然后依次装饰
@decol
@decol1
def send2():
    return '在学习'

print(send2())