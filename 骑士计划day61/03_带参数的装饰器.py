'''
带参数的装饰器
'''

from functools import wraps
from datetime import datetime

def out(k):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            if k == 'start':
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))
                r = func(*args,**kwargs)
            else:
                r = func(*args, **kwargs)
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))

            return r
        return inner
    return wrapper

# 1.wrapper = outer()  ==>2.inner = wrapper()  ==> 3.hell=inner
@out('start')
def hello():
    print('hello word')

hello()


