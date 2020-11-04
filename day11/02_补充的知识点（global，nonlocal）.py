
# 默认参数的陷阱
# def func(name,sex='男'):
#     print(name)
#     print(sex)
# func('alex')

# 陷阱只针对默认参数是可变的数据类型
# def func(name,alist=[]):
#     alist.append(name)
#     return alist
# ret = func('alex')
# print(ret)
# ret2 = func('太白金星')
# print(ret2)

# 如果你的默认参数指向的是可变的数据类型，name你无论调用多少次这个默认参数，都是同一个

# def func(a,list=[]):
#     list.append(a)
#     return list
# ret1 = func(10,)
# ret2 = func(20,[])
# ret3 = func(100,)
# print(ret1)
# print(ret2)
# print(ret3)




# 局部作用域的坑

# count = 0
# def func():
#     count += 1
#     print(count)
# func()


# 在函数中，如果你定义了一个变量，，但是在定义这个变量之前对其引用了，那么解释器认为，语法错误
# count = 0
# def func():
#     print(count)
#     cont = 3
# func()



# global
# 1.在局部作用域声明一个全局变量
# name = 'alex'
#
# def func():
#     name = '太白'
#     print(name)
# func()
# print(name)


# name = 'alex'
#
# def func():
#     global name
#     name = '太白'
#     print(name)
#
# print(name)    #会报错，因为函数没有执行
# globals()      #全局作用域
# func()
# print(name)

# 2.修改一个全局变量
# count = 1
# def func():
#     global count
#     count += 1
#
# print(count)
# func()
# print(count)


# nonlocal

# 1.不能操作全局变量

# 2.局部作用域，内层函数对外层函数的局部变量进行改变

def wrapper():
    count = 1
    def inner():
        nonlocal count
        count += 1
    print(count)
    inner()
    print(count)
wrapper()