# 2 1 3 2 1
# def func1():
#     print('in func1')
#
#
# def func2(x):
#     print('in func2')
#     return x
#
# def func3(y):
#     print('in func3')
#     return y
#
# ret = func2(func1)
# ret()
# ret2 = func3(func2)
# ret3 = ret2(func1)
# ret3()



# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
# print(func(1))
# print(func(2))
# print(func(3))


# def extendList(val,list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
#
# print('list1=%s' %(list1))
# print('list2=%s' %(list2))
# print('list3=%s' %(list3))


def func(num):
    count = 1
    for i in range(num,0,-1):
        count *= i
    return count

print(func(5))

# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[('红心'：2)，('黑桃':2)]

# 写代码完成9*9乘法表
