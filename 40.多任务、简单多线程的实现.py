"""
貌似应该放在线程特点前面

线程:CPU调度的基本单元
"""

# import time
# def song():
#     print('唱歌')
# def dance():
#     print('跳舞')

# song()
# time.sleep(2)
# dance()



#多线程
from threading import Thread
import time
def fun1():
    print('我是方法1')
    time.sleep(1)
    print('方法1执行完毕')
def fun2():
    print('我是方法2')
    time.sleep(1)
    print('方法2执行完毕')

# fun1()
# fun2()

if __name__ == '__main__':
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    # 守护线程 必须放在start之前 主线程执行结束 子线程也结束
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    # 阻塞主线程 join() 等子线程执行完之后结束
    t1.join()
    t2.join()
    print('全部执行完了')

