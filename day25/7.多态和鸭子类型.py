# 处处是多态，一切是对象
# 多态
# def add(int a,str b):
#     return a+b
#
# print(add(1,'djaklfda'))



# 一个类型表现出来的多种状态
# 支付 表现出的 微信支付和苹果支付这两种状态
# 在java情况下：一个参数必须制定类型
# 所以如果想让两个类型的对象都可以传，那么必须让这两个类继承自一个父类，在制定类型的时候使用父类来指定


# 鸭子类型
#


# class list:
#     def __init__(self,*args):
#         self.l = [1, 2, 3]
#         self.length = len(args)
#
#     def __len__(self):
#         n = 0
#         for i in self.l:
#             n+=1
#         return n
#
# l = [1,2,3]
# l.append(4)
#
# def len(obj):
#     return obj.__len__()


# 所有实现了__len__方法的类，在调用len函数的时候，obj都说是鸭子类型
# 迭代器协议__iter__ __next__ 是迭代器
# __add__
# 1+2
# '1'+'2'
# [1]+[2]


# super 是重要的
