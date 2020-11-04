# s1 = 'dskkdakdasfefsdfd';
# sum = 0
# for i in s1:
#     sum += 1
# print(sum)
# print(len(s1))

# l1 = [1,2,3,4,5,6]
# content = 0
# for i in l1:
#     content += 1
# print(content)


# 这样写代码太low
# 重复代码太多
# 代码的可阅读性差

# 函数式编程
# l1 = [1,2,3,4,5,6]
# s1 = 'dskkdakdasfefsdfd';
# def my_len(s):
#     content = 0
#     for i in s:
#         content += 1
#     print(content)
# my_len(s1)

# 函数：以功能（完成一件事）为导向，登录，注册，len，一个函数就是一个功能
# 随调随用
# 减少代码的重复性
# 增强代码的可读性

#
# def meet():
#     print('打开探探')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')

'''
结构：def 关键字，定义函数
    meet 函数名，与变量设置相同，具有可描述性
    函数体：缩进。函数中尽量不要出现print
    
'''
# 函数什么时候执行？
# 当函数遇到函数名加括号，函数才会执行
# meet()


# 函数的返回值
# s1 = 'afjdksafda'
# print(len(s1))

# def meet():
#     print('打开探探')
#     print('左滑一下')
#     return
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
#
# meet()

# return:在函数中遇到return直接结束函数

# def meet():
#     print('打开探探')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话...')
#     print('约....走起....')
#     return '妹纸一枚'

# ret = meet()
# print(ret)
# print(meet())

# return 将数据返回给函数的执行者，调用者


def meet():
    print('打开探探')
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    print('悄悄话...')
    print('约....走起....')
    return '妹纸',123,[22,33]
ret = meet()
print(ret,type(ret))

# return 返回多个元素，是以元组的形式返回给函数的调用者，执行者

'''
return 总结
    1.在函数中，终止函数
    2.return 可以给函数的执行者返回值
        1.return 单个值    单个值
        2.return 多个值   （多个值，）
'''
