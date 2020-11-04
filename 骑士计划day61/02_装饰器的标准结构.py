
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

# 此时会执行wrapper，所以wrapper必须定义在这一行
@wrapper
def hell():
    print('Hello word')

hell()