"""
with open 代码执行完会自动调用f.close 省略关闭文件步骤
"""

with open('files/test.txt',mode='r',encoding='utf-8') as f:
    print(f.readlines())

"""
二进制mode:rb
"""

#读取文件
with open('files/picture1.jpg',mode='rb') as f:
    img = f.read()
with open('files/picture1-copy.jpg',mode='wb') as f1:
    f1.write(img)


"""
os 目录模块 
import os
1.os.rename(旧名字,新名字)
2.os.remove(path) 删除文件
3.os.mkdir(path) 创建文件夹
4.os.rmdir(path) 删除文件夹
5.os.getcwd() 获取当前目录
6.os.listdir() 获取目录列表
"""

import os
print(os.listdir())