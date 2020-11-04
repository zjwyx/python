
# 判断是否都是一个可迭代对象？？
# 获取一个对象的所有方法,dir
# s1 = 'fjsdsl'
# l1 = [1,2,3]
# print(dir(s1))
# print(dir(l1))
# print('__iter__' in dir(s1))
# print('__iter__' in dir(range(10)))


# 小结
# 可迭代对象

# l1 = [1,2,3,4]
# for i in l1:
#     print(i)


# with open('文件1',encoding='utf-8',mode='w') as f1:
#     print('__iter__' in dir(f1) and '__next__' in dir(f1))

# s = 'kdkeikdw'
# print('__next__' in dir(s))



# 可迭代对象可以转化成迭代器
# s1 = 'dkskaliedk'
# # 转化成迭代器
# obj = iter(s1)
# # print(obj)
# # next() 取值
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

# l1 = [11,22,33,44,55,66]
# # 转化成迭代器,形成了迭代器赋值给了obj
# obj = iter(l1)
# print(obj)
# # 取值
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))



# 可迭代对象
# l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
# count = 0
# for i in l1:
#     if count == 4:
#         break
#     else:
#         print(i)
#     count += 1
#
# count = 0
# for i in l1:
#     if count == 6:
#         break
#     else:
#         print(i)
#     count += 1



# l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
# obj = iter(l1)
# for i in range(4):
#     print(next(obj))
#
# for i in range(6):
#     print(next(obj))


l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
# 将可迭代对象转化成迭代器
# 利用while循环模拟for循环对可迭代对象进行取值的机制
obj = iter(l1)
while 1:
    try:
        print(next(obj))
    except StopIteration:
        break