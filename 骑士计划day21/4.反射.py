# 3w 1h
# what 是什么
    # 反射 使用字符串数据类型的变量名来获取这个变量的值
# a = 1
# b = 2
# name = 'alex'
# print(a)
# why  为什么 三个场景
    # input()
        # 用户输入的如果是a，那么就打印1，如果输入的是b就打印2，如果输入的是name，就打印alex

    # 文件
        # 从文件中读出的字符串，就转化成变量的名字
    # 网络
        # 将网络传输的字符串转化成变量的名字
# where 在哪用
# how  怎么用

# 反射        ******
# hasattr()     # *****
# getattr()     # ******


# 反射类中的变量:静态属性，类方法，静态方法
# class Foo:
#     School = 'oldboy'
#     Country = 'Chine'
#     language = 'Chinese'
#
#     @classmethod
#     def class_method(cls):
#         print(cls.School)
#
#     @staticmethod
#     def static_method():
#         print('in foo')
#
#     def func(self):
#         print('wahaha')

# print(Foo.School)
# print(Foo.Country)
# print(Foo.language)


# 反射实现
# while 1:
#     inp = input('>>>')
#     print(getattr(Foo,inp))

# 解析getattr方法
# getattr(变量名：命名空间，字符串：属于一个命名空间内部的变量名)

# Foo.School
# getattr(Foo,'School')   # Foo.School

# Foo.class_method()
# print(getattr(Foo,'class_method'))
# getattr(Foo,'class_method')()
# print(Foo.class_method)

# Foo.static_method()
# getattr(Foo,'static_method')()  # Foo.static_method()
# Foo.func(1)
# getattr(Foo,'func')(1)      # Foo.func(1)
# print(hasattr(Foo,'func'))
# print(hasattr(Foo,'shaungwaiwai'))


# 反射实现
# while 1:
#     inp = input('>>>')
#     if hasattr(Foo,inp):
#         print(getattr(Foo,inp))

# 判断实现
# if inp == 'School':
#     print(Foo.School)
# if inp == 'Country':
#     print(Foo.Country)
# if inp == 'language':
#     print(Foo.language)



# 反射对象中的变量
# 对象属性
# 普通方法

# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eating(self):
#         print(f'{self.name} is eating')
#
# alex = Foo('alex_sb',83)
# print(getattr(alex,'name'))
# getattr(alex,'eating')()



# 反射模块中的变量
# os就是一个模块
# import os
# os.rename('a','b')
# print(getattr(os,'rename'))
# getattr(os,'rename')('b','a')






# 反射文件中的变量
a = 1
b = 2
name = 'alex'
def qqxing():
    print('qqxing')

# cls.xxx
# obj.xxx
# os.xxx

# 反射本文件中的变量，结论
# import sys
# # print(sys.modules['__main__'])
# print(getattr(sys.modules['__main__'],'a'))
# print(getattr(sys.modules['__main__'],'b'))
# # 变量，内置的变量
# print(__name__)



# setattr
# delattr
class Foo:
    Counter = 'qqxing'

def func():
    print('qqxing')
# Foo.School = 'odboy'
# 接受三个参数 命名空间 ‘变量名’ ‘变量值’
# setattr(Foo,'School','oldboy')
# print(Foo.__dict__)
# print(getattr(Foo,'School'))


# 一般没人往空间中添加函数
# setattr(Foo,'func',func)
# print(Foo.__dict__)
# Foo.func()
# getattr(Foo,'func')()


# delattr()
# del Foo.Counter
# delattr(Foo,'Counter')
# print(Foo.__dict__)



# hasattr()
# getattr()
# setattr()
# delattr()

# 反射类中的变量
# 反射对象的变量
# 反射模块中的变量
# 反射文件中的变量

# 用反射的场景
# input()
# 网络
# 文件
