# 1.你对python函数的理解
# 封装一个功能，提高代码的重用性，python的函数可以做很多事儿

# 2.函数中*args和**kwargs是什么意思
# 有问题


# 3.函数中return有什么作用
# 返回单个值
# 返回多个值 ，返回的是元组
# 结束函数，返回结果

# 4.解释一下迭代器，你在代码中如何获得一个迭代对象
# for循环，list()，next()

# 5.迭代器如何取值，迭代器中好处

# 6.什么是生成器，你在代码中如何获得一个生成器？

# 7.请构建一个生成器，里面的元素是1,4,9,16,25,36,49

# 8.解释一下名称空间与临时名称空间

# 9.请说一下你对闭包的理解，并说明在工作中哪里用过

# def outer():
#     name = 'alex'
#     # print(name)
#     def inner():
#         # name = 'wupeiqi'
#         print(name)
#     return inner
# inner = outer()
# inner()

# 闭包的作用：装饰器，做缓冲


# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(i)
# f(2)
# f(3,[3,2,1])
# f(3)


# l = [1,2,3]
# d = {'a':7,'b':8}
# def f(arg1,arg2,*args,**kwargs):
#     print(arg1,arg2,args,kwargs)
#
# f(1,2,3,'groovy')
# f(arg1=1,arg2=2,c=3,zzz='h1')


for i in range(5,0,1):
    print(i)


# 代码题











