'''
time 模块
三大对象
时间戳
格式化时间对象（9大字段）
字符串！！！
'''

import time
# 获取时间戳
# 时间戳：从时间元年（1970,1,1）到现在经过的秒数
# print(time.time())    # 1595168748.552

# 获取格式化时间对象:九个字段组成的
# 默认参数是当前系统时间的时间戳
# print(time.gmtime())
# print(time.localtime())
# print(time.gmtime(1))    # 时间元年过一秒后，对应的时间对象

# 格式化时间对象和字符串之间的转化
# s = time.strftime('%Y %m %d %H:%M:%S')
# print(s)

# 把时间字符串转换成时间对象
# s = time.strptime('2010 10 12','%Y %m %d')
# # s = time.strptime('2010','%Y')
# print(s)



# time模块的三大模块
# 格式化时间对象：time.struct_time
# 时间字符串
#
#
# 时间戳：从时间元年开始的秒数
# time.time()

# 时间戳转化成格式化时间对象
# time.gmtime()
# time.localtime()

# 格式化时间对象转化成时间戳
# time.mktime()

# 格式化时间对象转化成字符串
# time.strftime('%Y %m %d %H:%M:%S')
#
# # 字符串转换成格式化时间对象
# time.strptime('2010','%Y')



# 时间对象 ---> 时间戳
# print(time.mktime(time.localtime()))

# 暂停当前程序，睡眠xxx秒
for i in range(5):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(5)