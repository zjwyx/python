# 装饰器修复技术

from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print('这是新功能')
        func(*args,**kwargs)
    return inner

@wrapper
def f1(arg1,arg2):
    """
    这里写这个函数值做什么的
    :param arg1: 这个函数是什么类型的
    :param arg2: 这个函数是什么
    :return: None
    """
    print('嘿嘿')

print(f1.__doc__)
print(f1.__name__)

