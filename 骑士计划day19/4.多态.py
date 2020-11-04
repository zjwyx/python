
# 什么是多态:Animal类表现出了Dog，Cat两种类
# class Animal:pass
# class Dog(Animal):pass
# class Cat(Animal):pass
#
#
# 旺财 = Dog()



# 为什么要把多态单独列出来
# def func(str name,int age):
#     print(name,age)
# func(1,2)

# class Payment:pass
#
# class ApplePay(Payment):
#     def pay(self): pass
#
# class Alipay(Payment):
#     def pay(self): pass
#
# def pay(obj,money):
#     obj.pay()
#
#
# app = ApplePay()
# print(type(app))
# pay(app,123)
#
# alp = Alipay()
# pay(alp,345)


# 在java中运用多态来解决传参的时候 数据类型的规范问题









# str 是一个类
# a = '123'
# a = str('123')   str是一个类，str()就是实例化，a是一个对象，是str类的对象，a的type是str



# 什么是多态呢？
# 一个类表现出的多种状态，通过继承来实现
# 在java中的表现，在一个函数中需要给参数指定数据类型，如果这个地方可以接受两个以上类型的参数，
# 那么这些类型应该有一个父类，这个父类是所有子类对象的类型

# 在python中，函数的参数不需要指定数据类型，所以我们也不需要通过继承的形式来统一一组类的类型，
#       换句话说，所有的对象其实都是object类型，所以在python当中其实处处都是多态
# def func(a):
#     a既可以传猫也可以传狗，随便传任意类型




# 鸭子类型
#
# def len(obj):
# len()   # str list  tuple dict set
# index()   # str list  tuple
# print()    所有的对象都是鸭子类型
# 不是明确的通过继承实现的多态
# 而是通过一个模糊的概念来判断这个函数能不能接受这个类型的参数


# 背下来
# 写在本上
# 过两个月再反回来看，理解