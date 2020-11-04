'''
装饰器进阶
多个装饰器装饰同一个函数
'''

from functools import wraps
from datetime import datetime

# func：被装饰的函数
def wrapper(func):
    # 把func指向的函数的__doc__,__name__等属性都复制到inner上面
    @wraps(func)
    # args 和 kwargs 是被装饰函数的参数
    def inner(*args,**kwargs):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))
        func()
        print('新功能也可以写在这')
    return inner


def wrapper_b(func):
    # 把func指向的函数的__doc__,__name__等属性都复制到inner上面
    @wraps(func)
    # args 和 kwargs 是被装饰函数的参数
    def inner(*args,**kwargs):

        r = func(*args,**kwargs)
        return '<b>{}</b>'.format(r)

    return inner


def wrapper_i(func):
    # 把func指向的函数的__doc__,__name__等属性都复制到inner上面
    @wraps(func)
    # args 和 kwargs 是被装饰函数的参数
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)
        return '<i>{}</i>'.format(r)

    return inner

@wrapper_i
@wrapper_b
def hello():
    return 'Hell Word'

ret = hello()
print(ret)
