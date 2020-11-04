
# dic = {'k1':10,'k2':100,'k3':30}
# 利用内置函数匿名函数将dic按照值进行排序
# def func(a):
#     return dic[a]
# print(sorted(dic,key=lambda x:dic[x]))
# print(sorted(dic.items(),key=lambda x:x[1]))

# 利用内置函数匿名函数，计算列表的每个数的2倍
# [1,5,7,9.8]
# ret = map(lambda a:a*2,[1,5,7,9,8])
# print(list(ret))

# [5,8,11,9,15]
# 利用内置函数匿名函数，将值大于10的留下
# print(list(filter(lambda x:x>10,[5,8,11,9,15])))



# 递归函数

# 人理解函数，神理解递归

# def func():
#     print(666)
#     func()
#
# func()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# n = 1
# def func(x):
#     print(x)
#     x += 1
#     func(x)
#
# func(n)

# 默认递归参数：998
# import sys
# sys.setrecursionlimit(100000)
#
# n = 1
# def func(x):
#     print(x)
#     x += 1
#     func(x)
#
# func(n)


'''
alex 比 wusir 大两岁
wusir 比 日天 大两岁
日天 比 太白 大两岁
太白 24岁

'''
def age(n):
    if n == 1:
        return 24
    else:
        return age(n-1)+2

print(age(4))




'''

def age(4):
    if n == 1:
        return 24
    else:
        return age(n-1)+2

age(4)    age(1) + 2 + 2 + 2  = 24 + 2 + 2 + 2=30


def age(3):
    if n == 1:
        return 24
    else:
        return age(n-1)+2

age(3)  age(2) + 2


def age(2):
    if n == 1:
        return 24
    else:
        return age(n-1)+2

age(2)        age(1) + 2


def age(1):
    if n == 1:
        return 24
    else:
        return age(n-1)+2

age(4)     24

'''



'''
sum，reversed

min()
max()
sorted() 排序
map() 列表推导式中的循环
file() 列表推导式中的筛选
zip() 合并

匿名函数：多于内置函数结合使用
    lambda 参数：返回值
'''