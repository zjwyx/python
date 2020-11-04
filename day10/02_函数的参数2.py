# 形参角度
# 万能参数
# def eat(a,b,c,d):
#     print('我请你池，%s,%s,%s,%s' %(a,b,c,d))
# eat('鱼香肉丝','宫保鸡丁','水煮肉','熊掌')

# def eat(a,b,c,d,e,f):
#     print('我请你池，%s,%s,%s,%s,%s.%s' %(a,b,c,d,e,f))
# eat('鱼香肉丝','宫保鸡丁','水煮肉','熊掌','aaa','bbb')

# 急需要一种形参，可以接受所有的实参， 万能参数

# 万能参数：*args ，约定俗称：args
# 函数定义时，* 代表聚合，他将所有的位置参数聚合成一个元组赋值给了args

# def eat(*args):
#     print(args)
#     print('我请你池，%s,%s,%s,%s,%s.%s' %args)
# eat('鱼香肉丝','宫保鸡丁','水煮肉','熊掌','aaa','bbb')

# 写一个函数，计算你传入函数的所有的函数的和
# def max(*args):
#     return len(args)
# print(max(1,2,3,5))

# ** kwargs
# 函数在定义时， ** 将所有的关键字参数聚合到一个字典中，将这个字典赋值给了kwargs
# def func(**kwargs):
#     print(kwargs)
# func(name='alex',age=73,sex='laddboy')

# 万能参数：*args **kwargs
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func()



#  * 在函数的调用时，*代表打散
def func(*args,**kwargs):
    print(args)
    print(kwargs)
func(*[1,2],*[22,33])
func(**{'name':'太白'},**{'age':18})
# 等同于传关键字参数




# 形参角度的参数的位置
# args 得到实参的前提，sex必须重新赋值
# def func(a,b,*args,sex='男'):
#     print(a,b)
#     print(sex)
#     print(args)
# func(1,2,3,4,5)


# **kwargs 位置
# def func(a,b,*args,sex='男',**kwargs):
#     print(a,b)
#     print(sex)
#     print(args)
#     print(kwargs)
# func(1,2,3,4,5)

# 形参角度第四个参数：仅限关键字参数
def func(a,b,*args,sex='男',c,**kwargs):
    print(a,b)
    print(sex)
    print(args)
    print(c)
    print(kwargs)
# func(1,2,3,4,5,sex='女',name='alex',c=666)

# 形参角度最终的顺序：位置参数，*args，默认参数，仅限关键字参数，**kwargs

