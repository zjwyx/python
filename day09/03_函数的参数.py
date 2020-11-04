# def meet():
#     print('打开探探')
#     print('进行筛选，性别：女')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
#

# 函数的传参：让函数封装的这个功能，盘活
# 实参，形参

# 函数的定义：接受的参数形式参数
# def meet(sex):
#     print('打开探探')
#     print('进行筛选，性别：%s' %(sex))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')

# 函数的执行传的参数：实际参数
# meet('女')


# 函数的传参：实参，形参
# 实参角度：
# 1.位置参数：从左到右，一一对应
# def meet(sex,age,hobby):
#     print('打开探探')
#     print('进行筛选，性别：%s，年龄：%s，%s' %(sex,age,hobby))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
# meet('女','33','python技术好的')

# 写一个函数，只接受int的参数，函数的功能是将大的数返回
# def max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(max(100,300))

# 三元运算符，简单的if-else
# a = 10
# b = 20
# c = a if a > b else b
# print(c)


# 2.关键字参数.一一对应，顺序可以打乱
# def meet(sex,age,hobby,height,weight):
#     print('打开探探')
#     print('进行筛选，性别：%s，年龄：%s，技术：%s，身高：%s,体重：%s' %(sex,age,hobby,height,weight))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
# meet(sex='女',age='33',hobby='python技术好的',height=174,weight=100)

# 函数：传入两个字符串参数，将这两个参数拼接完成的结果返回

# def func(a,b):
#     return a + b
# print(func(b='太白',a='真丑'))


# 3.混和传参
# 位置参数一定要在关键字参数的前面
# def meet(sex,age,hobby,height,weight):
#     print('打开探探')
#     print('进行筛选，性别：%s，年龄：%s，技术：%s，身高：%s,体重：%s' %(sex,age,hobby,height,weight))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
#     return '筛选结果'
# meet('女','33',hobby='python技术好的',height=174,weight=100)



'''
实参角度
    1.位置参数 按照顺序，一一对应
    2.关键字参数，一一对应
    3.混和参数：位置参数一定要在关键字参数的前面
'''

# 形参角度
# 1.位置参数 与实参角度的位置参数是一种


# 写一个函数，检查列表的长度，如果列表的长度大于2，那么仅保留前两个长度的内容，，并将新内容返回个调用者
# def max_len(str):
#     if len(str) > 2:
#         return str[0:2]
#     else:
#         return str
#
# print(max_len([1,2,3,3,4]))


# 默认值参数
# 默认参数设置的意义，普遍经常使用的

# def meet(age,hobby='python技术好的',sex='女'):
#     print('打开探探')
#     print('进行筛选，性别：%s，年龄：%s，技术：%s' %(sex,age,hobby))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')

# meet(age='33',hobby='python技术好的')
# meet('33',sex='男')

# 形参角度
# 1.位置参数
# 2.默认参数  （经常使用的参数）


# 三元运算（三目运算）
# a = 1
# b = 2
# h = a-b if a>b else a+b
# print(h)

c = 100
d = 200
h =  c if c>d else d
print(h)