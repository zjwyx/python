
# 广义上的封装

# class 类名:
#     def 方法1(self):pass

# 是为了只有这个类的对象才能使用定义在类中的方法


# 狭义上的封装
# 把一个名字藏在类中
# class Goods:
#     # 私有的静态变量
#     __discount = 0
#     print(__discount)


# 在类的外部不能引用私有的静态变量
# print(Goods.__discount)

# 类中的静态变量和方法名在程序加载的过程中就已经执行完了，不需要等待调用
# 在这个类加载完成之前，Goods这个名字还没有出现在内存空间中
# 私有的静态属性可以在类的内部使用，用来隐藏某个变量的值


# class Goods:
#     # 私有的静态变量
#     __discount = 0
#     # 变形，_类名__私有变量
#     # print(__discount)

# 在类的外部不能引用私有的静态变量
# print(Goods.__dict__)
# # 编程规范的角度上出来，我们不能在类的外部使用私有的变量
# print(Goods._Goods__discount)











# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#
#     def name(self):
#         return self.__name
# zhuge = Student('诸葛',210)
# print(zhuge.name())
# print(zhuge.age)




# class Goods:
#     # 私有的静态变量
#     __discount = 0.7
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#
#     def price(self):
#         return self.__price * Goods.__discount
#
# apple = Goods('APPLE',5)
# print(apple.price())


# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#         self.pwd = self.__getpwd()
#
#     def __getpwd(self):
#        return hash(self.__password)
#
# obj = User('alex','alex3714')
# print(obj.username,obj.pwd)


# 类中私有成员：
    # 私有的静态变量
    # 私有的对象属性
    # 私有的方法


# 私有变量能不能在外部被定义？
# class A:
#     # 在类的内部会犯发生变形
#     # _A__country
#     __country = 'China'
#
# print(A.__dict__)
#
# A.__Language = 'China'
# print(A.__dict__)


# 私有变量能不能被继承？
# class A:
#     __country = 'China'
#     def __init__(self,name):
#         # _A__name
#         self.__name = name
#
# class B(A):
#     def get_name(self):
#         # B' object has no attribute '_B__name'
#         return self.__name
#
#
# b = B('alex')
# # b.get_name()
# print(b.__dict__)


# 我为什么要定义一个私有变量呢？
    # 我不想让你看到这个值
    # 我不想让你修改这个值
    # 我想让你在修改这个值的时候有一些限制，保证了数据的安全
    # 有些方法或者属性不希望被子类继承



# 广义上的封装 把树先进函数都放到类中
# 狭义上的封装，定义私有成员
