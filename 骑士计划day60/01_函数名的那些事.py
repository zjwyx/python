# def func():
#     print('永远都不要高估自己')
#
# # 函数的内存地址
# print(func)
# # 当成变量赋值给a
# a = func
# print(a)
# # 通过a变量调用函数
# a()
#
#
#
# # 把函数当成参数
# def f1(arg):
#     arg()
#
# f1(func)
#
# # 函数可以当返回值
# def f2():
#     # f3 = 函数的定义
#     def f3():
#         print('我是f3')
#     return f3
# # 把内部定义的f3赋值给了ret
# ret = f2()
# ret()   #相当于执行了f3




def fa():
    print('fa')

def fb():
    print('fb')

def fc():
    print('fc')

list1 = [fa,fb,fc]

for i in list1:
    # i表示列表中每一个元素
    i()
























