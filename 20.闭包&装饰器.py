"""
递归函数
闭包
装饰器
"""

#递归
def add(n):
    if(n==1):
        return 1
    return n + add(n-1)
print('100个数加起来为:',add(100))


#闭包
def outer():
    n = 10
    def inner():
        print(n)
    return inner

outer()()

#装饰器
def test02():
    print('发送信息')

def test(fn):
    print('开始注册')
    print('登录')
    fn()
test(test02)