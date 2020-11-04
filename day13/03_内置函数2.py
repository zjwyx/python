# eval() 剥去字符串的外衣，运算里面的代码，有返回值
# s1 = '1+3'
# print(s1)
# print(eval(s1))

# 网络传输的str，input 输入的时候，sql注入等等绝对不能使用eval

# exec 与eval几乎一样，代码流
# msg = '''
# for i in range(10):
#     print(i)
# '''
# # print(msg)
# exec(msg)

# hash 哈希值
# print(hash('jdkjkd'))


# help 帮助
# s1 = 'dafdsa'
# print(help(str.upper))


# callable 判断一个对象是否可被调用
# def func():
#     pass
# # func()
# print(callable(func))







# # bin：将十进制转换成二进制并返回。
# print(bin(10))
# # oct：将十进制转化成八进制字符串并返回。
# print(oct(10))
# # hex：将十进制转化成十六进制字符串并返回
# print(hex(13))


# divmod()  **
# print(divmod(10,3))

# round() 保留浮点数的小数位数
# print(round(3.1415926,2))

# pow()  一个参数的幂  **
# print(pow(2,3,3))

# bytes()  ***
# s1 = '太白'
# b = bytes(s1,encoding='utf-8')
# print(b)


# ord 输入字符找该字符编码的位置
# print(ord('a'))
# chr() 输入位置数字找出其对应的字符
# print(chr(97))

# repr() 返回一个对象的string形式（原形毕露）  ***
# s1 = '台标'
# print(repr(s1))
# msg = '我叫%r' %s1
# print(msg)


# all() 可迭代对象中，全部是true才是true
# l1= [1,2,'太白','']
# print(all(l1))

# any() 可迭代对象中，有一个true才是true
# l1= [1,2,'太白','']
# print(any(l1))







# print()
# print(1,2,3)
# sep 分隔符
# print(1,2,3,sep='&')
# print(1,end=' ')
# print(2)


# list
# l1 = [1,2,3]
# l2 = list('dsafdafd')
# print(l2)


# dict 创建字典的几种方式
# 直接创建
# 元祖的解构
# dic = dict([(1,'onr')])
# dic = dict(one=1)
# print(dic)
# fromkeys
# update
# 字典推导式


# abs() 绝对值  ***
# print(abs(-8))

# sum() 求和
# l1 = [i for i in range(0,10)]
# print(sum(l1))
# print(sum(l1,100))

# reversed() 返回的是一个翻转的迭代器
# l1 = [i for i in range(0,10)]
# l1.reverse()   列表的方法
# print(l1)

# l1 = [i for i in range(0,10)]
# obj = reversed(l1)
# print(obj)
# print(l1)
# print(list(obj))


# zip 拉链方法
# l1 = [1,2,3,4,5]
# tul = ('太白','b哥','德刚')
# s1 = 'abcd'
# obj = zip(l1,tul,s1)
# print(obj)
# for i in obj:
#     print(i)
# print(list(obj))


# *********************************************** 一下方法最最最重要
l1 = [33,2,1,54,7,-1,-9]
# print(min(l1))
# 以绝对值的方式取最小的
# l2 = []
# func = lambda a: abs(a)
# for i in l1:
#     l2.append(func(i))
# print(min(l2))
# def abss(a):
#     '''
#     第一次：a = 33 以绝对值取最小值33
#     第一次：a = 2 以绝对值取最小值2
#     '''
    # return abs(a)
# print(min(l1,key=abss))
# 凡是可以加key的，他会自动的将可迭代对象中的每一个元素按照顺序传入key对应的函数中
# 已返回值比较大小


# dic = {'a':3,'b':3,'c':1}
# 求出值最小的键值对
# min默认会按照字典的键去比较大小
# def func(a):
#     return dic[a]
# print(min(dic,key=func))


# l2 = [('太白',108),('alex',73),('wusir',35),('昊天',41)]
# def func1(a):
#     return a[1]
# print(min(l2,key=func1))
# print(min(l2,key=func1)[0])
# print(min(l2,key=func1)[1])



# sorted  加key
# l1 = [22,33,1,2,8,7,6,5]
# l2 = sorted(l1)
# print(l1)
# print(l2)


# l2 = [('太白',108),('alex',73),('wusir',35),('昊天',41)]
# def func1(a):
#     return a[1]
# # 返回一个列表
# print(sorted(l2,key=func1))
# print(sorted(l2,key=func1,reverse=True))



# filter 列表推导式的筛选模式
# l1 = [2,3,4,1,6,7,8]
# ret = filter(lambda x: x>3,l1)
# print(ret)
# 迭代器取值，next，for ，list
# print(list(ret))


# map() 列表推导式的循环模式
# l1 = [1,4,9,16,25]
# ret 是一个迭代器
# ret = map(lambda x:x**2,l1)
# print(ret)
# print(list(ret))


# reduce()
from functools import reduce
def func(x,y):
    '''
    第一次：x y：1,2 x+y=3 记录3
    第二次：x = 3,y=3  x+y=6 记录6
    第三次：x = 6，y=4，x+y=10

    '''
    return x*10 + y*10
l1 = reduce(func,[1,2,3,4])
print(l1)

