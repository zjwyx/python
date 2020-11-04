
# 新式类
# 在python3.x版本中，所有的类都是新式类
# 所有的新式类都有一个默认的父亲：object
# class Person1:pass
# class Person2():pass
# class Person3(object):pass

# p = Person2()    # __init__初始化方法
# print(Person1.__bases__)
# print(Person2.__bases__)
# print(Person3.__bases__)

# python 2.7
# 经典类 和 新式类 并存
# class Student:pass    # 经典类
# class Student(object):pass


# 继承了object的类就是新式类
# 在py3中所有的类都是新式类
# 在py2中既有新式类又有经典类


# 多继承的顺序，在新式类和经典类之间的区别

# class A:
#     def func(self):
#         print('A')
#
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
#
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
#
# class D(B,C):
#     def func(self):
#         super().func()
#         print('D')

# d = D()
# d.func()
# print(D.mro())
# D().func()
# B.func()


# 新式类中，
    # 所有的多继承关系寻找方法的顺序：------ 遵循广度优先（数据结构中有）
    # 继承object
    # mro方法
    # super:super不是单纯的找父类，而是遵循 mro 顺序的


# 经典类
# python2.x
# 不主动继承object
# 经典类在找父类中方法的过程中：遵循 -- 深度优先
# 不提供mro和super

# 写上object就成了新式类，就继承c
# 不写object就成了经典类，就继承a
