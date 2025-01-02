# 检测数据类型的方法 type()
num  = 1
print(type(num))


'''
数值类型
int 整形
float 浮点数
boolean 布尔型,布尔值可当做整型
complex 复数型 z = a + bj  a是实部,b为虚部,j为虚数单位,不用深究

'''
isTrue = True
print(isTrue + 1)


ma = 1 + 2j
print(ma)


'''
字符串类型,单双引号都可以
'''
str = '测试字符串'
print(str)

duohang = """我是第一行
我是第二行
我是第三行
"""
print(duohang)




"""
格式化输出，占位符
1. %  
%s 字符串常用
%d 整数常用
%f 浮点数 默认六位小数,四舍五入
%% 输出一个

2. f

"""

name = 'bingbing'
print('我的名字:%s' %name)

age = 18
print('我的年龄:%d' %age)
print('我的名字%05d' %age) # 输出几位,不足用0补全

cc = 1.254
print("cc的值为: %f" %cc)
print("cc的值为: %.2f" %cc)

# 占位符
print('我是100%%的1%%' % ())


a1 = "wgg"
a2 = 29
print(f"我的名字是:{a1},年龄为:{a2}")