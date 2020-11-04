# for i in "123456789":
#     print(i)

# 虽然上面的缩进的内容都叫代码块，但是他不是python中严格定义的代码块
# python中真正意义的代码块是什么？
# 一个模块，一个函数，一个类，一个文件等都是一个代码块
# def func():
#     print(333)
#
# class People:
#     print(222)


#  交互模式下，每一行都是一个代码块
# >>>>>i1 = 100 可以理解为这一行在一个文件中

# 二： id  is  ==
# name = "alex"
# name1 = "alex"
# print(name)
# print("alex" == "alex");
# 内存中的地址值
# print(id(name),id(name1))
# 在内存中id都是唯一的，如果两个变量指向的值的id相同，就证明他们在内存中是同一个
# is 判断的是两个变量的id值是否相同
# 如果is是true，==一定是true

# 三 小数据池（缓冲机制，驻留机制）

# 小数据池，python对内容做的一个优化
# 将-5,256的整数，以及一定规则的字符串，提前在内存中创建了池。容器，容器里固定的放了这些数
# 为什么这么做？？
# 1.节省内存
# 2.提高性能与效率
# i1 = 100
# i2 = 100
# print(id(i1),id(i2))
# print(id(i1) is id(i2))
# print(i1 is i2)
# 小数据池的应用的数据类型：整数，字符串，bool值
# 一定规则的字符串？

s1 = "alex@"
s2 = "alex@"
print(s1 is s2)