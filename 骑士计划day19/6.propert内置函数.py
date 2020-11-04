
# property 是一个装饰器函数
# 所以的装饰器函数都怎么用呢？在函数，方法，类的上面一行直接@装饰器的名字
# 装饰器的分类
    # 装饰函数
    # 装饰方法：property
    # 装饰类


# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     # 装饰器，把一个方法伪装成一个属性
#     @property
#     def name(self):
#         return self.__name
# zhuge = Student('诸葛',20)
# print(zhuge.name)


from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return self.r ** 2 * pi

    @property
    def perimeter(self):
        return 2 * self.r *pi


c1 = Circle(5)
print(c1.area)
