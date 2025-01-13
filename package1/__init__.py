print('package1的__init__.py')


#导入保内的其它模块
# from package1 import module1
# from package1 import login
from package1 import single

# module1.register()

#__all__ 相当于导入[]里面定义的模块
__all__ = ['module1','login']