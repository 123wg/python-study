"""
 文件操作
 open() 打开文件,创建一个file文件，默认以只读方式打开
 read(n) 从文件中读取的数据长度,不传或者负值读取所有内容
 write() 将指定内容写入文件
 close() 关闭文件

 readline() 读取一行数据

属性
文件名.name 获取文件名
文件名.mode 返回文件的访问模式
文件名.closed 判断文件是否关闭
"""

f = open(file = 'files/test.txt',encoding='utf-8')
print(f)
print(f.name)
print(f.mode)
print(f.closed)

# ss = f.read()
# print(ss)

while(True):
    text = f.readline()
    if(text == ''):
        break
    print(text)
f.close()