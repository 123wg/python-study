"""
进程语法结构
multiprocessing 提供了Process类代表进程对象

Process(target,args=())
- target 子进程要执行的任务
- args 元组传参
- kwargs 字典传参

常用方法
start() 开启子进程
is_alive() 判断紫禁城是否还活着
join() 主进程等待子进程执行结束

常用属性
name: 进程别名,默认Process-N
pid: 进程编号
"""

from multiprocessing import Process
import os

def song():
    print('子进程p1编号:',os.getpid()) #获取当前进程编码
    print('主进程编号:',os.getppid()) #获取主进程编号
    print('开始唱歌')
def dance():
    print('开始跳舞')

if __name__ == '__main__':
    p1 = Process(target=song,name='子进程1')
    p2 = Process(target=dance,name='子进程2')
    p1.start()
   
    print(p1.name)
    print('子进程p1编号:',p1.pid)

    p1.join() #主进程处于等待状态 p1处于执行状态
    print('p1存活状态',p1.is_alive())

    p2.start()

    print('主进程编号:',os.getpid())