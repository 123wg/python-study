"""
readlines() 按照行的方式一次读取数据，返回列表

访问模式
r 只读
r+ 可读写文件
w 只写 先清空,再写入添加内容
w+ 先写在读 会覆盖
a 只写 追加内容

文件定位操作
tell() 显示文件内当前位置及 文件指针当前位置
seek(offset,whence) 移动文件读取指针到指定位置
offset:偏移量，表示要移动的字节数
whence:起始位置，表示移动字节的参考位置，默认是0,0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表文件结尾作为参考位置
seek(0,0) 将文件指针移到开头
"""

f = open('files/test.txt',mode='w+',encoding='utf-8')
f.write('\nhelloworld!\n我是一个小伙子')

pos = f.tell()
print(f'文件当前位置{pos}')

f.seek(0,0)

text = f.readlines()

for i in text:
    print(i)

f.close()


