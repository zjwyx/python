'''
collections模块

namedtuple()命名元组
defaultdic()默认字典
Counter()计数器

'''


# from collections import namedtuple
# namedtuple()
# Rectangle = namedtuple('Rectangle_class',['length','width'])
# #
# r = Rectangle(10,5)
# # 通过属性访问元组的元素
# print(r.length)
# print(r.width)
#
# # 通过索引的方式访问元素
# print(r[0])
# print(r[1])


# defautldict
# 创建一个字典的方式
# d = {'name':'alex'}
# d = dict(['name','alex'])
# d = {k:v for k,v in [(1,2),(2,5)]}
# print(d)
# from collections import defaultdict
#
# d = defaultdict(int,name='alex',age=20)
# print(d['name'])
# print(d['age'])
# # addr = 0也会被添加
# print(d['addr'])
# print(d)


# 自定义函数充当第一个参数
# 要求：不能有参数
from collections import defaultdict

def f():
    return 'hell'


d = defaultdict(f,name='alex',age=20)
print(d['addr'])
print(d)


# Counter:计数器
from collections import Counter
c = Counter('abcdefabcccccdd')
print(c.most_common(3))
