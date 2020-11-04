import re
# ret = re.findall('\d+','19740ash9310uru')
# print(ret)
#
# ret1 = re.search('\d+','19740ash9310uru')
# # 变量
# print(ret1)
# if ret1:
#     print(ret1.group())



# 预习一个现象并且找到答案 - 分组有关系()
# findall 还是按照完整的正则进行匹配，只是显示括号里匹配到的内容

# ret = re.findall('9(\d)\d','19740ash9310uru')
# print(ret)
#
#
# # search 还是按照完整的正则进行匹配，显示也显示匹配到的第一个内容，但是我们可以通过给group方法传参
# # 来获取具体文组中的内容
# ret1 = re.search('9(\d)(\d)','19740ash9310uru')
# # 变量
# print(ret1)
# if ret1:
#     print(ret1.group())
#     print(ret1.group(1))





# findall
    # 去找所有符合条件的，优先显示分组中的

# search 只取第一个符合条件的，没有优先显示这件事
    # 得到的结果是一个变量
    # 变量，group()的结果 完全和 变量 group(0)的结果一致
    # 变量 group(n) 的形式来指定获取第n个分组中匹配到的内容

# 为什么search中不需要分组优先，而在findall中需要？



# 为什么要用分组，以及findall的分组优先到底有什么好处？
# exp = '2-3*(5+6)'
# # a+b 或者a-b并且计算他们的结果
#
# ret = re.search('(\d)+[+](\d+)',exp)
# print(ret)
# print(ret.group(1))
# print(ret.group(2))
# print(int(ret.group(1)) + int(ret.group(2)))






# 如果我们查找的内容在一个复杂的环境中
# 我们要查找的内容没有一个突出，与众不同的特点，甚至会和不需要的杂乱的数据混和在一起
# 这个时候我们就需要把所有的数据统计出来，然后对这个数据进行筛选，把我们真正需要的数据对应的正则表达式用 圈起来
# 选择我们就可以筛选出真正需要的数据了





# 什么是爬虫
    # 通过代码获取到一个网页的源码
    # 要的是源码中嵌套中网页上的内容 - 正则

import requests
ret = requests.get('https://bj.lianjia.com/zufang/')
print(ret.content.decode('utf-8'))

# 分组和findall
    # 为什么要用分组
    # 把想要的内容放分组里
# 如何取消分组
    # 如果在写正则的时候由于不得已的原因，导致不要的内容也得写在分组类
    # (?:) 取消这个分组的优先显示


# 作业
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# 1.匹配出wahaha，banana，qqxing内容
# 2.匹配出a，b，h1这样的内容



# a = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'