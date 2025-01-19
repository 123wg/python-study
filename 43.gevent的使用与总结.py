"""
gevent: 遇到IO操作时会自动切换，属于主动切换
使用:
gevent.spawn(函数名):创建协程对象
gevent.sleep(): 耗时操作
gevent.join(): 阻塞，等待某个协程执行结束
gevent.joinall(): 等待所有协程对象都执行结束再退出，参数是一个协程对象列表
"""

#gevent
# import gevent
# import time

# def sing():
#     print('在唱歌')
#     gevent.sleep(2)
#     print('唱完歌了')
# def dance():
#     print('在跳舞')
#     gevent.sleep(2)
#     print('跳完舞了')

# # sing()
# # dance()

# if __name__ == '__main__':
#     #创建协程对象
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     #阻塞，等待协程执行结束
#     g1.join() #等待g1对象执行结束
#     g2.join()



#joinall 使用
# import gevent
# def sing(name):
#     for i in range(5):
#         gevent.sleep(1)
#         print(f'{name}在唱歌，被送走的第{i}次')

# if __name__ == '__main__':
#     gevent.joinall([
#         gevent.spawn(sing,'wgg'),
#         gevent.spawn(sing,'bingbing')
#     ])


#monket补丁:拥有在模块运行时替换的功能
import gevent
from gevent import monkey
import time
monkey.patch_all() #将用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep()代码
# 注意:monkey.patch_all()必须放在被打补丁者前面
def sing(name):
    for i in range(5):
        time.sleep(1)
        print(f'{name}在唱歌，被送走的第{i}次')

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing,'wgg'),
        gevent.spawn(sing,'bingbing')
    ])


"""
总结:
线程是CPU调度的基本单位，进程是资源分配的基本单位

进程、线程和协程对比
进程：切换需要的资源最大，效率最低
线程：切换需要的资源一般，效率一般
协程：切换需要的资源最小，效率高

多线程适合IO密集型操作(文件操作、爬虫)，多进程适合CPU密集型操作(科学计算、视频高清解码、计算圆周率)

进程、线程、协程都是可以完成多任务的，根据实际开发需要选择使用
"""