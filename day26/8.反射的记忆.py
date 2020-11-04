# 1.反射对象的 实例变量 绑定方法
# 2.反射类的 静态变量 其他方法
# 3.模块中的所有变量
    # 被导入的模块
    # 当前执行的py文件 - 脚本

# class A:
#     Role = '治疗'
#     def __init__(self):
#         self.name = 'alex'
#         self.age = 84
#
#     def func(self):
#         print('wahaha')
#         return 666
# a = A()
# # 反射对象的实例变量
# print(getattr(a,'name'))
# # 反射对象的绑定方法
# print(getattr(a,'func')())
# print(getattr(A,'Role'))

# 引用模块中的任意的变量
# import a
# print(a.sww())
# print(a.lst)
# print(getattr(a,'sww'))
# getattr(a,'sww')()
# print(getattr(a,'lst'))
# print(getattr(a,'dic'))



# 反射本模块中的名字
# import sys
# cat = '小a'
# dog = '小b'
# def pig():
#     print('小p')
#
# ret = getattr(sys.modules['__main__'],'dog')
# print(ret)
