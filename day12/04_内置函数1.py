# python 提供了68个内置函数
# 今天讲的这部分大部分了解即可
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
def func():
    pass
# func()
print(callable(func))


# bin：将十进制转换成二进制并返回。
# oct：将十进制转化成八进制字符串并返回。
# hex：将十进制转化成十六进制字符串并返回

# print(bin(10),type(bin(10)))  # 0b1010 <class 'str'>
# print(oct(10),type(oct(10)))  # 0o12 <class 'str'>
# print(hex(10),type(hex(10)))  # 0xa <class 'str'>
print(bin(10))
print(oct(10))
print(hex(10))







