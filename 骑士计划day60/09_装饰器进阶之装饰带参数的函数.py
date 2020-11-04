# 装饰带参数的函数

def wrapper(func):
    def inner(*args,**kwargs):
        print('开始')
        r = func(*args,**kwargs)
        print(r)
        print('结束')
        return r
    return inner

@wrapper
def my_sum(x,y):
    print('我是mu_sum函数')
    return x+y

# inner(10,20)
ret = my_sum(10,20)
print(ret)
