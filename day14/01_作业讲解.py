# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda :num+10,lambda :num+100,lambda :num+100]
#     result1 = v4[1]()
#     result2 = v4[2]()
#     print(result1,result2)
# func()

# map,filter,列表推导式的循环模式和过滤模式，匿名函数写在map(函数，列表)里面
# min，max(列表，函数)

# 用map来处理字符串列表，把列表中所有人都变成sb，比如alex_sb
# name = ['old','alex','wusir']
# ret = map(lambda a:a+'_sb',name)
# print(ret)
# print(list(ret))

# 用map来处理下述1，然后用list得到新的一个列表，列表中每一个人的名字都是sb结尾
# l = [{'name':'alex'},{'name':'y'}]
# ret = map(lambda a:a['name']+'sb',l)
# print(list(ret))


# 用filter来处理，得到股市价格大于20的股市名字
# shares = {
#     'IBN':36.6,
#     'Lenovo':23.2,
#     'oldboy':21.2,
#     'ocean':10.2
# }
# def func(a):
#     return shares[a] > 20
# ret = filter(func,shares)
# print(list(ret))
# def func(a):
#     for i in a:
#         if a[i] > 20:
#             print(a[i])
#
# func(shares)

# 有一下三种数据
# l1 = [1,2,3,4,5]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','******')
# print(list(filter(lambda x:x[0] > 2 and len(x[-1]) >= 4,zip(l1,l2,tu))))


# l1 = [
#     {'sales_valumn':0},
#     {'sales_valumn':108},
#     {'sales_valumn':337},
#     {'sales_valumn':475},
#     {'sales_valumn':396},
#     {'sales_valumn':172},
#     {'sales_valumn':9},
#     {'sales_valumn':58},
#     {'sales_valumn':272},
#     {'sales_valumn':456},
#     {'sales_valumn':440},
#     {'sales_valumn':239}
# ]
# def func(a):
#     return a['sales_valumn']
# print(sorted(l1,key=func))
#
# # 按照列表中的每个字典的values大小进行排序，形成一个新的列表
#
# def func1(a):
#     return a['sales_valumn']
# # 返回一个列表
# print(sorted(l1,key=func1,reverse=True))
# print(sorted(l1,key=func1))

# 九个函数地址值
# func = lambda :x
# v = [lambda :x for x in range(10)]
# 只要这样写，在内存中x 已经定格在9值
# print(v)
# print(v[0])
# print(v[0]())


# 生成器表达式
v = (lambda :x for x in range(10))
# # print(v)
# # print(v[0])
# # print(v[0]())
# 第一个函数的内存地址
# print(next(v))
# 第二个函数的值
# print(next(v)())


# 面试题
# list(map(str,[1,2,3,4,5,6,7,8,9]))
# # ['1'.....'9']



# 写一个函数完成三次函数
# 用户的用户名，密码从一个文件register中取出
# register文件包含多个用户名，密码，用户名，密码通过；隔离，每个人的用户名密码占用一行
# 完成三次登录，三次验证不成功则登录失败，登录失败返回false
# 登录成功返回true

# def new_list():
#     dic={}
#     with open('register',encoding='utf-8') as f1:
#         for line in f1:
#             line_list = line.strip().split('|')
#             dic[line_list[0]] = line_list[1]
#     return dic
#
# # print(new_list())
#
# def login():
#     count = 0
#     dic_line = new_list()
#     while count < 3:
#         username = input('请输入用户名:').strip()
#         password = input('请输入密码:').strip()
#         if username in dic_line and password == dic_line[username]:
#             print('登录成功')
#             return True
#         else:
#             print('登录失败')
#         count += 1
