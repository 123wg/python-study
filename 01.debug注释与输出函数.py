# 多行注释可以是三个单引号和多引号
"""
我是多行注释
print(123)
"""

'''
我也是多行注释
'''

print('123')



# 单行注释是#

'''
print(*values,sep)
*values 可以输出多个值,添加逗号
sep 间隔多个值
end 设定以xx结尾,默认为\n
'''
print(1,2,3,sep = '-',end='')