"""
* 匹配前一个字符出现0次或者无限次，可有可无 --常用
+ 匹配前一个字符出现1次或者无限次，即至少一次 --常用
? 匹配前一个字符出现1次或0次                --常用
{m} 匹配前一个字符出现m次
{m,n} 匹配前一个字符出现m到n次
"""
import re

res1 = re.match('\d*[a-z]\d*','154w12')
print(f'*匹配结果:{res1.group()}')

res2 = re.match('\d+','25w12')
print('+匹配结果:',res2.group())

res3 = re.match('\d?','25w12')
print('?匹配结果:',res3.group())

res4 = re.match('\d{3}','254w12')
print('{m}匹配结果:',res4.group())

res5 = re.match('\d{3,5}','2554876w12')
print('{m,n}匹配结果:',res5.group())



"""
匹配开头结尾
^ 匹配字符串开头,表示对...取反
& 匹配字符串结尾
"""

res6 = re.match('^[a-z]','wgg')
print('匹配开头:',res6.group())

#^在中括号中表示不匹配,即匹配[]包含的字符之外的字符
res7 = re.match('[^py]','wgg')
print('中括号不匹配:',res7.group())

res8 = re.match('.*$','wgs45')
print('匹配结尾:',res8.group())