# def wrapper(f):
#     # f = func
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
#
#
# @wrapper   # func = wrapper(func)
# def func():
#     print('in func')
# func()  # inner()





# 看代码写结果
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         return ret
#     return inner
#
# def func():
#     print(333)
#
# print(444)
# func()
# print(555)


# 编写装饰器，在每次执行被装饰器之前打印一句‘每次执行被装饰器函数之前都得经过这里’
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print('次执行被装饰器函数之前都得经过这里')
#         ret = f(*args, **kwargs)
#         return ret
#
#     return inner
#
# @wrapper
# def func():
#     print(333)
#
# func()



# 为函数写一个装饰器，把函数的返回值加100，然后返回

# def wrapper(f):
#     def inner(*args,**kwargs):
#         ret = f(*args,**kwargs)
#         return ret+100
#     return inner
#
# @wrapper
# def func():
#     return 7
#
# result = func()
# print(result)


# 装饰器，把函数循环五次
# def wrapper(f):
#     def inner(*args,**kwargs):
#         for i in range(5):
#             f(*args,**kwargs)
#     return inner
# @wrapper
#
# def func():
#     print('in func')
# func()





#
import time


def wrapper(f):
    def inner(*args,**kwargs):
        with open('alex',encoding='utf-8',mode='a') as f1:
            struct_time = time.localtime()
            f1.write(f'北京时间:{time.strftime("%Y-%m-%d %H:%M:%S",struct_time)}执行了{f.__name__}函数\n')
        ret = f()
        return ret
    return inner

@wrapper

def wcnb():
    print('in wcnb')

wcnb()
time.sleep(2)
wcnb()
time.sleep(1)
wcnb()


# def wrapper():
#     pass
#
# def func(f):
#     print(f.__name__)
# func(wrapper)
