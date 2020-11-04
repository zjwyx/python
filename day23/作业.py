# 统计作业完成度，难点
# 作业笔记
    # 写一个题的用时
    # 遇到的问题
    # 解决思路




# 读程序，标出程序的执行过程，画出内存图解，说明答案和为什么
# (1)
# class A:
#     # 静态属性 存储在类的命名空间里的
#     Count = '中国'
#     # 绑定方法 存储在类的命名空间里的
#     def __init__(self,name,age,country):
#         self.name = name
#         self.age = age
#         # self.Count = country
#
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
# A.Count = '日本人'
# a.Count = '英国人'
# print(a.Count)
# print(b.Count)
# print(A.Count)


# (2)
# class A:
#     # 静态属性 存储在类的命名空间里的
#     Count = ['中国']
#     # 绑定方法 存储在类的命名空间里的
#     def __init__(self,name,age,country):
#         self.name = name
#         self.age = age
#         # self.Count = country
#
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
# A.Count[0] = '日本人'
# # 三个日本人
# print(a.Count)
# print(b.Count)
# print(A.Count)


# (3)
# class A:
#     # 静态属性 存储在类的命名空间里的
#     Count = '中国'
#     # 绑定方法 存储在类的命名空间里的
#     def __init__(self,name,age,country):
#         self.name = name
#         self.age = age
#         self.Count = country
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
# A.Count = '日本人'
# # 印度
# print(a.Count)
# # 泰国人
# print(b.Count)
# # 日本人
# print(A.Count)


# (4)
# class A:
#     # 静态属性 存储在类的命名空间里的
#     Count = '中国'
#     # 绑定方法 存储在类的命名空间里的
#     def __init__(self,name,age,country):
#         self.name = name
#         self.age = age
#         # self.Count = country
#
#     def Count(self):
#         return self.Count
#
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国人')
#
# print(a.Count)
# print(b.Count())


# 第二大题：基于圆形类实现一个圆环类，要求接受参数 外圆半径和内圆半径
# 完成方法：计算环形面积和环形周长（公式自己上网查）
# 要求：借助组合，要求组合圆形类的对象完成需要

# 第三大题：继续完成计算器和优化功能