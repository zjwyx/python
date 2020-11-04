# 装饰器带参数
def mougecanshu(arg):
    def wrapper(func):
        def inner(*args,**kwargs):
            print('欢迎VIP用户进入{}专栏'.format(arg))
            func(*args,**kwargs)
        return inner
    return wrapper

# @wrapper()
@mougecanshu('电影')
def movie():
    print('这是电影专栏')


@mougecanshu('体育')
def sport():
    print('这是体育专栏')

movie()
sport()

