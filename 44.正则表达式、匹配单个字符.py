"""
模块 import re

re.match(pattern,string) 匹配以xx开头的字符串
pattern:匹配的正则表达式
string:要匹配的字符串


"""
import re
res = re.match('冰冰','冰冰永远18岁')

print(res)
print(res.group())

"""
匹配单个字符
. 匹配任意一个字符，除\n以外 --常用
[] 匹配[]中列举的字符        --常用
\d 匹配数字0-9              --常用
\D 匹配非数字               --常用
\s 匹配空白、空格和tab键     
\S 匹配非空白
\w 匹配单词字符，即a-z,A-Z,0-9,_,汉字 --常用
\w 匹配非单词字符 
"""

res1 = re.match('.','hello')
print(res1.group())

res2 = re.match('[1234]','423')
print(res2.group())
res3 = re.match('[0-9]','126')
print('匹配首字母为0-9的',res3.group())

res4 = re.match('.\d','123')
print(res4.group())

res5 = re.match('\D\d[0-9].','s123')
print(res5.group())

res6 = re.match('\d\s\d.','1 23')
print(res6.group())

res7 = re.match('\S','123')
print('\S匹配',res7.group())

res8 = re.match('\w','_D123')
print('\w',res8.group())

res9 = re.match('\W','.D123')
print('\w',res9.group())
