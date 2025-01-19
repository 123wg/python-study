"""
特点
1.线程的执行是无序的
2.线程间共享资源
3.
"""

# 线程执行无序，根据CPU调度决定
import time
from threading import Thread
def sing(name):
    print(f'{name}在唱歌')
    time.sleep(1)
    print('唱完歌了')

def dance(name2):
    print(f'{name2}在跳舞')
    time.sleep(1)
    print('跳完舞了')

if __name__ == '__main__':
    name = 'wgg'
    t1 = Thread(target = sing,args=(name,))
    t2 = Thread(target = dance,args=(name,))
    t1.start()
    t2.start()


import threading
def task():
    print('当前线程是:',threading.current_thread().name) # 显示当前线程对象名
if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=task)
        #启动子线程
        t.start()