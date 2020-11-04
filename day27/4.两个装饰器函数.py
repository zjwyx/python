# 被装饰的方法会成为一个类方法
# classmethod

# class Goods:
#     __discount = 0.8
#     def __init__(self):
#         self.__price = 5
#         self.price = self.__price * self.__discount
#     # 把一个对象绑定的方法，修改成一个 类方法
#     @classmethod
#     def change_discount(cls,new_discount):
#         # print(cls,Goods)
#         cls.__discount = new_discount
#
#
#
# # 定义了一个方法，默认传self，但这个self没被使用
# # @classmethod   把一个对象绑定的方法 修改成一个 类方法
# # 第一，在方法中任然可以引用类中的静态变量
# # 第二，可以不使用实例化对象，就直接用类名在外部调用这个方法
#
# # 什么时候用@classmethod？
#     # 1.定义了一个方法，默认传self，但这个self没被使用
#     # 2.并且你在这个方法用到了当前的类名，或者你准备使用这个类的内存空间的名字的时候
#
# # 类方法可以通过类名调用
# Goods.change_discount(0.6)
# apple = Goods()
# print(apple.price)
#
# # # 修改折扣 0.6
# # 类方法可以通过对象名调用
# apple.change_discount(0.5)
# apple2 = Goods()
# print(apple2.price)



# python核心编程/基础教程/流畅的python/数据结构与算法(机械工业出版社)/cook book

# import time
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#     @classmethod
#     def today(cls):
#         struct_t = time.localtime()
          # 实例化
#         date = cls(struct_t.tm_year,struct_t.tm_mon,struct_t.tm_mday)
#         return date
#
# date的对象 = Date.today()






# 被装饰的方法会成为一个静态方法
# @staticmethod

class User:
    pass

    # 本身是一个普通的函数，被挪到类的内部执行，那么直接给这个函数添加@staticmethod装饰器就可以了
    @staticmethod
    def login():
        print('登录的逻辑')
        # 在函数的内部既不会用到self变量，也不会用到cls类

obj = User()
User.login()
obj.login()


class A:
    count = '中国'
    def func(self):
        print(self.__dict__)

    @classmethod
    def class_func(cls):
        print(cls)

    @staticmethod
    def stat_func():
        print('普通函数')

    @property
    def name(self):
        return 'wahaha'

# 总结：
# 能定义到类中的方法
# 静态变量           是个所有的对选哪个共享的变量  由对象|类调用  但是不能重新赋值
# 绑定方法           是个自带self参数的函数  由对象调用
# 类方法            是个自带cls参数的函数   由对象 类调用
# 静态方法          是个啥都不带的普通函数   有对象|类调用
# @property属性    是个伪装成属性的方法   由对象调用，但不加括号
