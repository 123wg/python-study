""""
抛出异常 raise
步骤:
1.创建一个Exception('xxx')对象 xxx--异常提示信息
raise 抛出这个对象
"""

# raise Exception('wgg抛出了一个异常')
def login():
    pwd = input('请输入密码')
    if(len(pwd) > 6):
        return '密码输入成功'
    raise Exception('长度不足六位,请重新输入')

try:
    print(login())
except Exception as e:
    print(e)


"""
模块
一个py文件就是一个模块
分类:
random
time
os
logging

第三方模块
pip install 模块名

自定义模块
"""

"""
模块导入方式
1.import 模块名
使用 模块名.功能
2.from...import...
from...import * 导入所有模块


"""

import package1.pytest as pytest

print(pytest.name)

from package1.pytest import name
print('pytest中导入的模块',name)