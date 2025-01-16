"""
线程特点：
1.线程间共享资源
2.资源竞争
"""

from threading import Thread,Lock
import time

#全局变量
li = []
#写入数据
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(0.01)
    print('写入的数据为',li)
def rdata():
    print('读取的数据为',li)

if __name__ == '__main__':
    #创建子线程
    t1 = Thread(target=wdata)
    t2 = Thread(target=rdata)
    #开启子线程
    t1.start()
    #阻塞线程 解决先读取后写入的问题 会等待t1执行结束
    t1.join()
    t2.start()


#资源竞争
# a = 0
# b = 1000000
# def add():
#     for i in range(b):
#         global a
#         a+=1
#     print('第一次:',a)
# # add()

# def add2():
#     for i in range(b):
#         global a
#         a+=1
#     print('第二次:',a)
# # add2()

# if __name__ == '__main__':
#     t1 = Thread(target=add)
#     t2 = Thread(target=add2)
#     t1.start()
#     t2.start()


"""
线程同步

互斥锁:对共享数据锁定,保证多个线程访问共享数据不会出现数据错误,保证同一时刻只能有一个线程去操作
acquire() 上锁
release() 释放锁
ps:必须成对出现,否则会出现死锁
"""

a1 = 0
b1 = 1000000
lock = Lock()
def add3():
    lock.acquire()
    for i in range(b1):
        global a1
        a1+=1
    print('第一次:',a1)
    lock.release()
# add()

def add4():
    lock.acquire()
    for i in range(b1):
        global a1
        a1+=1
    print('第二次:',a1)
    lock.release()
# add2()

if __name__ == '__main__':
    t3 = Thread(target=add3)
    t4 = Thread(target=add4)
    t3.start()
    t4.start()



"""
进程:
1.进程是操作系统分配资源的最小单位,是程序的一次执行过程，是分配给CPU的时间片段
2.进程中可以创建多个线程

进程的状态
1.就绪状态:等待CPU执行
2.执行状态:正在执行
3.等待(阻塞)状态:等待条件满足
"""
