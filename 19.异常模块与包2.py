"""
1.别名
import 模块名 as 别名

2.as给功能取别名
from 模块名 import 功能 as 别名

导入多个功能，使用逗号隔开

3.内置全局变量 __name__
if __name__ == "__main__"
用来控制py文件在不同的应用场景执行不同的逻辑
3.1.文件在当前程序执行自己 __name__ == '__main__'
3.2.文件被当做模块被其他文件导入: __name__ = 模块名
"""

import pytest as pt
print(pt.name)

pt.test()


"""
包
项目结构中的文件夹
与普通文件夹的区别:含有__init__.py文件
"""