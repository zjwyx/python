# print(111)
# import tbjx
# print(222)

# import tbjx
# import tbjx
# import tbjx

# 第一次导入模块发生三件事
# import tbjx
# print(tbjx.name)
# tbjx.read()


import tbjx
# name = 'alex'
# print(name)
# print(tbjx.name)


# def read1():
#     print(666)
#
# tbjx.read1()

# name = '日天'
# tbjx.change()
# # 日天
# print(name)
# # barry
# print(tbjx.name)


'''
tbjx.py

name = '太白金星'
def change():
    global name
    name = 'barry'
'''

# import tbjx as sm
# print(sm.name)


# 了解

# 起始方法
# res = input('请输入：')
# if res == 'mysql':
#     import mysql1
#     mysql1.mysql()
# elif res == 'oracle':
#     import oracle1
#     oracle1.oracle()

# list.index()
# str.index()
# tuple.index()

# 起别名
res = input('请输入：')
if res == 'mysql':
    import mysql1 as sb

elif res == 'oracle':
    import oracle1 as sb

'''后面还有很多'''
# 统一接口，归一化思想
sb.db()