# x = {
#     'name':'alex',
#     'Values':[
#         {
#             'timestamp':1517991992.94,
#             'values':100
#         },
#         {
#             'timestamp':1517992000.94,
#             'values':200
#         },
#         {
#             'timestamp':1517992014.94,
#             'values':300
#         },
#         {
#             'timestamp':1517992744.94,
#             'values':350
#         }
#     ]
# }
#
# print([[i['timestamp'],i['values']] for i in x.get('Values')])


# colors = ['black','white']
# sizes = ['S','M','L']
# l1 = []
# for color in colors:
#     for size in sizes:
#         l1.append((color,size))
# print(l1)


# def chain(*args):
#     for it in args:
#         for i in it:
#             yield i
# g = chain('abc',(1,2,3))

# 怎样让生成器产生值？
# next for循序 转化成list
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# print(list(g))



# def demo():
#     for i in range(4):
#         yield i
#
# g = demo()
# # 生成器
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g1))
# print(list(g2))


# 重点（面试题）
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g = test()

for n in [1,10]:
    g = (add(n,i) for i in g)

# 迭代器只有遇到next，for，list才会执行
print(list(g))



























































