'''
datetime:日期时间模块

封装了一些和日期，时间相关的类

date
time
datetime
timedate
'''


import datetime
# date类：

# d = datetime.date(2010,10,10)
# print(d)

# 获取date对象的各个属性
# print(d.year)
# print(d.month)
# print(d.day)

# time类

# t = datetime.time(10,48,59)
# print(t)
# # time类的属性
# print(t.hour)
# print(t.minute)
# print(t.second)


# datetime
# dt = datetime.datetime(2010,11,11,11,11,11)
# print(dt)



# datetime中的类，主要是用于数学计算的
# timedelta：时间的变化率
# td = datetime.timedelta(days=1)
# print(td)
# # 参与数学运算
# # 创建时间对象
# # date.datetime.timedelta
# d = datetime.date(2010,10,10)
# res = d + td
# print(res)


# 时间变化量的计算是否会产生进位？
# t = datetime.datetime(2010,10,10,10,10,59)
# td = datetime.timedelta(seconds=3)
# print(t + td)


# 练习：计算某一年的二月份有多大？
# 普通的算法，根据年份计算是否是闰月，是29天，否28
# 用datetime模块
# 首先创建出指定年份的3月1号，然后让他往前走一天
# year = int(input('请输入年份:'))
# # 创建指定年份的date对象
# d = datetime.date(year,3,1)
# # 创建一天的时间
# td = datetime.timedelta(days=1)
# res = d - td
# print(res)


# 和时间段进行运算的结果，类型？？
# d = datetime.datetime(2010,10,10,10,10,10)
d = datetime.timedelta(seconds=20)
td = datetime.timedelta(days=1)
res = d + td

d1 = datetime.date(2010,10,10)
res2 = d1 + res
print(res2)