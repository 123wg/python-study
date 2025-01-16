"""
进程间不共享全局变量
"""

# from multiprocessing import Process
# import time


# li = []
# def wrate():
#     for i in range(10):
#         li.append(i)
#         # time.sleep(0.1)
#     print('写入的数据是',li)

# def rdata():
#     print('读取的数据是',li)

# if __name__ == '__main__':
#     p1 = Process(target = wrate)
#     p2 = Process(target = rdata)
#     p1.start()
#     p1.join()
#     p2.start()

"""
Queue 队列
q.put() 放入数据
q.get() 取出数据
q.empty() 判断队列是否为空
q.qsize() 返回当前队列包含的消息数量
q.full() 判断队列是否满了
"""

# from queue import Queue

# q = Queue(2)
# q.put('小伙子')
# q.put('你是谁啊')
# print(q.qsize())
# print(q.full())
# print(q.get())
# print(q.get())
# print(q.empty())


"""
进程使用队列-共享数据
"""
from multiprocessing import Process,Queue
import time

li = ['张三','李四','王五']
q = Queue()
def wdata(q1):
    for i in range(5):
        print(f'{i}已经被放入')
        q1.put(i)
        li.append(i)
        time.sleep(0.1)
    print('写入的数据',li)

def rdata(q2):
    while True:
        #判断是否为空
        if q2.empty():
            break
        else:
            print('取出数据',q2.get())
    print('读取数据',li)

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target = wdata,args=(q,))
    p2 = Process(target = rdata,args=(q,))
    p1.start()
    p1.join() #等待队列中的数据放入完成
    p2.start()