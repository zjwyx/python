
# 圆形类
# bmi

# 学生类
# class Student:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,new):
#         if type(new) is str:
#             self.__name = new
#
# zhuge = Student('诸葛')
# print(zhuge.name)

# zhuge.name = '猪猪'
# print(zhuge.name)

# 只有当被property装饰的方法
# 又实现了一个同名的方法
# 且被setter装饰器装饰了
# 且 在对被装饰的方法 赋值的时候，就出发被setter装饰器装饰的方法

# 用来保护一个变量 在修改的时候能够添加一些保护条件
# c++每一个变量




# class Goods:
#     __discount = 0.8
#     def __init__(self,price):
#         self.__price = price
#         self.name = 'apple'
#
#     @property
#     def price(self):
#         return self.__price * Goods.__discount
#
#     @price.setter
#     def price(self,new):
#         self.__price = new
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
# app = Goods(10)
# print(app.price)
#
# del app.price
#
# # app.price = 8
# # print(app.price)
#
#
# print(app.__dict__)
# del app.name
# print(app.__dict__)
# 对于属性的操作
# 1.查看属性  @property
# 2.添加 修改属性    @price.setter
# 3.删除属性




# 一个方法被伪装成属性之后
# 应该可以执行一个属性的增删改查
# 那么增加和修改，就对应这被setter装饰的方法：这个方法又有一个必传的参数new，表示赋值的时候等号后面的值
# 删除一个属性，对应有 被deleter装饰的方法：这个方法并不能执行的时候真的删除这个属性，而是你在代码中执行什么就有什么效果


# class A:
#     def __init__(self):
#         self.__f = open()
#
#     @property
#     def f(self):
#         return self.__f
#
#     @f.deleter
#     def f(self):
#         self.__f.close()
#         del self.__f



# 类方法 的 特点
# 只是用类中的资源，这个资源可以直接使用类名引用的使用，那这个方法应该改为一个类方法
# 静态属性
# 普通方法
# 类方法
# property方法


# apple = Goods(10)
# # banana = Goods(20)
# apple.change_discount(0.7)
# print(apple.price)



class Student:

    @staticmethod
    def login(username,password):
        print('in login')

Student.login('username','password')



# 类
    # 静态属性          类  所有的对象都统一拥有的属性
    # 类方法           类   如果这个方法涉及到操作静态属性，类方法，静态方法                        cls表示类
    # 静态方法          类   普通方法，不使用类中的资源，也不使用对象的资源（命名空间），一个普通的函数   没有默认参数
    # 方法            对象                                                                  self表示对象
    # property方法    对象   伪装成一个属性                                                    self便是对象
