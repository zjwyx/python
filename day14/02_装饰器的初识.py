# 装饰器的本质：闭包   *******
# 装饰器：装饰，装修，房子就可以住，如果装修，不影响你住，而且体验更加，让你的生活中增加了很多功能，洗澡，看电视
# 器：工具
# 开放封闭原则
# 开放：对代码的扩展开放的。更新地图，加新枪等等
# 封闭：对源码的修改是封闭的。
#   闪躲，就是功能，一个函数

# 装饰器，完全遵循开放封闭原则
# 装饰器，在不改变原函数的代码以及调用方法的前提下，为其增加新的功能
# 装饰器就是一个函数





# 版本一：大壮，写一些代码测试一下index函数的执行效率
# import time
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
#
# def dariy():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆日记页面')

# print(time.time())
# 1970年。格林威治事件

# print(111)
# time.sleep(3)
# print(222)

# 版本一有问题，如果测试别人的代码，必须重新赋值粘贴
# start_time = time.time()
# index()
# end_time = time.time()
# print(end_time - start_time)

# start_time = time.time()
# index()
# end_time = time.time()
# print(end_time - start_time)



# 版本二，解决代码重复使用的问题

# import time
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
#
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记页面')
#
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print(f'函数的测试时间为：{end_time - start_time}')
# timmer(index)

# 版本二还有问题，原来index函数函数源码没有变化，给原函数添加了一个新的功能测试原函数的执行效率的功能
# 满足了开放封闭原则吗？原函数的调用方式改变了



# 版本三,不能改变原函数的调用方法
# import time
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
#
#
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'函数的测试时间为：{end_time - start_time}')
#     return inner
# # timmer(index)    # index()
# # ret = timmer(index)
# # ret()
# index = timmer(index)
# index()


# def func():
#     print('in func')
#
#
# def func1():
#     print('in func1')
#
# func()
# func = 666
# func(0)




# 版本四，具体研究
# import time
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
#
#
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'函数的测试时间为：{end_time - start_time}')
#     return inner
#
# index = timmer(index)
# index()




# 版本五，python做了一个优化，提供了一个语法糖的概念(标准的装饰器)
# import time
# # timmer装饰器
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'函数的测试时间为：{end_time - start_time}')
#     return inner
#
# # index = timmer(index)
# @timmer
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
# index()
#
#
# @timmer
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记页面')
# dariy()






# 版本六：被装饰函数带返回值
# import time
# # timmer装饰器
# def timmer(f):
#     def inner():
#         start_time = time.time()
#
#         # print(f'这个是f():{f()}')
#         r = f()
#         end_time = time.time()
#         print(f'函数的测试时间为：{end_time - start_time}')
#         return r
#     return inner
#
# # index = timmer(index)
# @timmer
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园首页')
#     return 666
# ret = index()
# # index()  ----> inner()函数的返回值
# # 加上装饰器不应该改变原函数的返回值，所有666应该返回给我下面的ret
# # 但是下面的这个ret实际接收的是inner函数的返回值，而666返回给的是装饰器里面的f(),也就是r
# # 我们现在要解决的就是将r给inner的返回值
# # print(ret)



# 版本七：被装饰函数带参数返回值
import time
# timmer装饰器
def timmer(f):
    def inner(*args,**kwargs):
        # 元组，字典
        # 函数的定义：* 聚合 args=()
        start_time = time.time()

        # print(f'这个是f():{f()}')
        r = f(*args,**kwargs)
        # 函数的执行：* 打散：f(*args)----->f(*('李',18))---->f('李'，18)
        end_time = time.time()
        print(f'函数的测试时间为：{end_time - start_time}')
        return r
    return inner


@timmer   # index = timmer(index)
def index(name):
    '''有很多代码'''
    time.sleep(2)
    print(f'欢迎{name}登陆博客园首页')
    return 666

index('纳钦')  # inner('纳钦')
@timmer
def dariy(name,age):
    '''有很多代码'''
    time.sleep(3)
    print(f'欢迎{age}岁{name}登陆日记页面')
dariy('李舒淇',18)




# 标准版的装饰器
def wrapper(f):
    def inner(*args,**kwargs):
        '''添加额外的功能：执行被装饰函数之前的操作'''
        ret = f(*args,**kwargs)
        '''添加额外的功能：执行被装饰函数之后的操作'''
        return ret
    return inner

