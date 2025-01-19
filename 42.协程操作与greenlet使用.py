"""
协程
定义:微线程,python中另外一种实现多任务的方式，只不过比线程更小，占用更小执行单元。 
自带CPU上下文。这样只要在合适的时机，可以把一个协程切换到另一个协程。只要这个过程中保存或恢复CPU上下文那么程序还是可以运行的
"""

#简单实现协程
# import time
# def task1():
#     while True:
#         yield '哈哈哈'
#         time.sleep(1)
# def task2():
#     while True:
#         yield '嘿嘿嘿'
#         time.sleep(1)

# if __name__ == '__main__':
#     t1 = task1()
#     t2 = task2()
#     while True:
#         print(next(t1))
#         print(next(t2))

"""
使用场景
1. 如果一个线程中有IO操作比较多，用协程
2. 适合高并发处理

greenlet:是一个由C语言实现的协程模块。通过设置switch()来实现任意函数之间的切换。
注意:
1.greenlet属于手动切换，当遇到IO操作，程序会阻塞，不能进行自动切换
"""

#greenlet实现任务切换
from greenlet import greenlet
def sing():
    print('在唱歌')
    g2.switch()
    print('唱完歌了')
def dance():
    print('在跳舞')
    print('跳完舞了')
    g1.switch()

if __name__ == '__main__':
    #创建协程对象 greenlet(任务名)    
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    g1.switch() #切换到g1中去运行
    g2.switch()

