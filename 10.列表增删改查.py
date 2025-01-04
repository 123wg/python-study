"""
和ts数组一样，数据类型可不一样

"""
arr = [1,2,3,4]
# 循环
# for index,item in enumerate(arr):
#     print(index,item)

#切片 不包括结尾的
print(arr[0:3])

#下标取值
print(arr[2])

#添加元素 append() expend() insert()
arr.append(5); # 添加一个
print(arr)

arr.extend([2,7,6]) #添加可迭代对象
print(arr)

arr.insert(2,10) # 插入 类似splice
print(arr)

#查找运算
#in 判断指定元素是否在列表中，存在返回true否则返回false
#not in 和 in相反
print(10 not in arr)

##index 和 count等和字符串相同

#删除元素 del pop()  remove()
li = [1,2,3]
del li

#默认删最后一个，参数为下标
arr1 = [1,2,3,7]
arr1.pop(1)
print(arr1)

#remove根据元素值删除,不存在时报错
arr1.remove(7)
print(arr1)

# 排序 sort() reverse()倒序
arr2 = [5,4,7,8,1]
arr2.sort()
print(arr2)

arr2.reverse()
print(arr2)


#列表推导式
"""
格式一:[表达式 for 变量 in 列表]
格式二:[表达式 for 变量 in 列表 if 条件]
"""
arr3 = [1,5,4,7,8,9]

[print(i*5) for i in arr3]

print(arr3)
[print(i) for i in arr3 if(i//4 == 1)] #整除4为1的