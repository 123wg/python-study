class Washer:
    height = 800 #相当于静态属性

    def wash(self):
        print(self)
        print('洗衣服')


print('洗衣机高度为',Washer.height)

""""
实例化对象: 对象名 = 类名()  
"""

washer = Washer()
washer.wash()
print(washer)  


"""
实例方法
至少有一个self参数
"""
