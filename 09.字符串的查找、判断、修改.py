"""
find(字符串,开始位置下标,结束位置下标) 同ts数组的find，返回下标，否则返回-1
index(同上),检测子字符串是否包含在子字符串中，如果在就返回这个子字符串开始位置的下标，否则就会报错
count() 返回子字符串 在整个字符串中出现的次数，没有返回0
split() 分割字符串

replace() 替换
"""

name = 'wggbingbibg,ceshi'
print(name.find('i'))
# print(name.index('p'))
print(name.count('i'))

name.replace('wg','wggg')
print(name)

print(name.split('g'))