# 自己调用自己
# count = 0
# def func():
#     global count
#     count += 1
#     print(count)
#     if count == 3:return
#     func()
#     print(456)
#
# func()


# RecursionError
# 递归的最大深度1000层:为了节省内容空间，不要让用户无限使用内容空间
# 1.递归要尽量控制次数，如果需要很多层递归才能解决问题，不适合用递归解决
# 2.循环和递归的关系
    # 递归不是万能的
    # 递归比起循环来说更占用内存
# 修改递归的最大深度
    # import sys
    # sys.setrecursionlimit(10000000)


# 你的递归函数，必须停下来
# 递归函数是怎么停下来的？递归3次结束整个函数

# count = 0
# def func():
#     global count
#     count += 1
#     print(count)
#     if count == 3:return
#     func()
#     print(456)
#
# func()
#
#
# def func():
#     global count
#     count += 1
#     print(count)
#     if count == 3:return
#     func()
#     print(456)
#
# def func():
#     global count
#     count += 1
#     print(count)
#     if count == 3:return
#     func()
#     print(456)


# if count / 10 商5余3

# def func(count):
#     count += 1
#     print(count)
#     if count == 5:return 5
#     # if divmod(count,10) == (5,3):return
#     # ret = func(count)
#     return func(count)
# print('---->',func(1))



# 一个递归函数要想结束，必须在函数内写一个return并且return的条件必须是一个可达到的条件
# 并不是函数中有return，return的结果就一定能够在调用函数的外层接受到

# def func(count):
#     count += 1
#     print(count)
#     if count == 5:return 5
#     return func(count)
# print('---->',func(1))


# 1.计算阶乘
# 2.os模块，查看一个文件下的所有文件，这个文件下面还有文件夹，不能用walk
# 3.os模块，计算一个文件下所有文件的大小，这个文件下面还有文件夹，不能用walk
# 2.计算斐波那契数列
# 3.三级菜单


def func(count):
    if count == 1:
        return count
    else:
        return count * func(count-1)

print(func(5))

