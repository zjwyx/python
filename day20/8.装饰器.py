# 什么是装饰器
# 为什么要有装饰器
# 为什么不能改变原函数的调用方式
    # 开放封闭原则
    # 我们提前写好一个功能，让别人使用的时候直接使用就能使用就能完成相应的功能


# 登录
# 计算函数的执行时间


# 写了很多的函数
# 添加日志：在时间调用了什么函数
import time

def logger(path):
    def log(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)

            with open(path,mode='a',encoding='utf-8') as f:
                msg = '%s 执行了%s'%(time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__)
                f.write(msg)
            return ret
        return inner
    return log

@logger('auth.log')
def login():
    print('登录的逻辑')

@logger('auth.log')
def reginter():
    print('注册的luoij')

@logger('operat.log')
# show_goods = log(show_goods)
def show_goods():
    print('查看所有商品信息')

@logger('operat.log')
def add_goods():
    print('商品加入购物车')




# login()
# add_goods()


# 登录和注册信息 写到auto.log文件中
# 所有的购物信息，写到operat.log文件中


# 带参数的装饰器
# 有100个 函数，分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有的时候不需要
# 希望能通过修改一个变量，能控制这100个函数的装饰器是否执行
