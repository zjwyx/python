# 简述 生成器，迭代器，可迭代对象 以及应用场景
# 生成器 就是 迭代器
# 是程序员自己写的：生成器函数 生成器表达式
# 可迭代对象：含有__iter__的方法对象都是可迭代的
    # 可迭代对象都可以被迭代的
    # 之所以可以被迭代是因为iter(obj)可以让这个对象变成一个迭代器
# 应用场景：
    # 大量数据需要处理，能够有效的节省内存空间
        # 爬虫，文件处理，网络上大量的数据返回的
    # 可以取到这个对象中的每一项
# 批量处理任务，批量显示结果


# 列举面向对象中带爽下划线的特殊方法，如：__new,__init__
# 先执行new，在执行init
# __call__方法 是让一个对象变成 callable的对象
# 实现内置call方法 会让对象()调用这个call方法
# class A:
#     def __call__(self, *args, **kwargs):
#         print('执行call了')
#
# obj = A()
# # obj()
#
# print(callable(A))
# print(callable(obj))

# Flask源码分析：call
# 元类 单例模式 call

# 面试题，请用尽量多的方式来实现单例模式
# new
# 类装饰器来实现
# 元类 + call
# 模块导入


# 异常处理写法以及如何主动抛出异常
# try:
#     pass
# except: 异常的类型
#     处理异常
# else：
# finally:

# raise 异常类型（提示信息）


# 简述 gevent模块的作用和应用场景
# 协程模块 基于greenlet实现的
# 能够在遇到io操作的时候主动切换
# 高io行的操作 实现单线程的并发操作 -- 爬虫


# 列举常见的关系型数据库和非关系型数据库都有哪些？
# 关系型数据库：mysql，oracle，sql server，sqlit
# 非关系型数据库：redis memcache mongodb nosql
