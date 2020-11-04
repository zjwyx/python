# 仅限关键字参数
# def func(a,b,*args,c):
#     print(a,b)
#     print(c)
#
# func(1,2,3,4,c=666)

# *
# a,b,*c = (1,2,3,4,5,6)
# # print(a,b,c)

# a,*b,c = [11,22,33,44,55,66,77]
# print(a,b,c)


# def func():
#     global name
#     name = 'alex'

# func()
# print(name)
# print(name)
# func()

# name = '太白'
# def func():
#     global name
#     name = 'alex'
#
#
# print(name)
# func()
# print(name)
# print(name)
# print(name)
# print(name)
# print(name)




# def func():
#     name = '太白'
#     def inner():
#         nonlocal name
#         name = 'alex'
#     print(name)
#     inner()
#     print(name)
# func()


# def func():
#     pass
# func()


# 其中a也是自由变量
# def wapper(a):
#     name = 'alex'
#     def inner():
#         print(name)
#         print(a)
#     return inner
#
# ret = wapper('烧饼')
# # 获取自由变量
# print(ret.__code__.co_freevars)


# 装饰器的基本步骤
# def wrapper(f):
#     def inner(*args,**kwargs):
#         ret = f(*args,**kwargs)
#         return ret
#     return inner

