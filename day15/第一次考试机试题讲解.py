# 第一题
# lis = [['哇',['how',{'good':['am',100,'99']},'太白金星'],'i']]
# 列表lis中的’am‘变成大写
# print(lis[0][1][1]['good'][0].upper())
# 列表中的100通过数字相加在在转化成字符串的方式变成’10010
# print(str(lis[0][1][1]['good'][1]) + '10')


# 第二题
# dic = {'k1':'v1','k2':['alex00',20],(1,2,3):{'k3':{'2',100,'wer'}}}
# 将k3对应的值的最后面添加一个元素23
# 将k2对应的值的第0个位置插入元素a
# 将（1,2,3）对应的值的添加一个键值对k4：v4

# 第三题
# 实现一个整数加法器（多个数相加）
# 如：content = input('请输入内容')用户输入：5+9+6+12+13，然后进行分割在计算


# 第四题：请写一个电影票程序，现在上映的电影列表如下
# lst = ['复仇者联盟4','驯龙高手3','金瓶梅','老男孩','大话西游']
# 由用户给每个电影投票，最终将投票的信息公布出来
# 要求：
# 用户可以持续投票，用户输入序号，进行投票，比如输入序号1，给金瓶梅投票
# 每次投票成功，显示给哪部电影投票成功
# 退出程序后，要显示每个电影的投票数
# 建议最终的结果为这种形式{'复仇者联盟4':90,'驯龙高手3':6,'金瓶梅':30,'老男孩':20,'大话西游':88}
# dic = {}
# while 1:
#     for index,movie_name in enumerate(lst):
#         print(f'序号：{index+1},电影名称{movie_name}')
#     num = input('请输入投票的电影序号：').strip()
#     if num.isdecimal():
#         num = int(num)
#         if 0<num<=len(lst):
#             if lst[num - 1] not in dic:
#                 dic[lst[num - 1]] = 1
#             else:
#                 dic[lst[num - 1]] += 1
#         else:
#             print('超出范围，重新输入')
#     elif num.upper() == 'Q':break
#     else:
#         print('输入有误，请重新输入')
#
# for movie_name,count in dic.items():
#     print(f'电影{movie_name},最终票数为{count}')

# 第五题
# 有文件t1.txt里面的内容为：
# id，name，age，phone，job
# 1，alex，22,13651504680，it 2，wusir，23,13302320533，Teacher 3，太白，15,133325353233，it
# 利用文件操作，，将其构造成入下数据类型
# [{'':1,'name':'alex','age':'22','phone':13651504680,'job':IT}]



# 第六题
# 按要求完成以下操作
list3 = [
    {
        'name':'alex',
        'hobby':'抽烟'
    },
    {
        'name':'alex',
        'hobby':'喝酒'
    },
    {
        'name':'alex',
        'hobby':'烫头'
    },
    {
        'name':'alex',
        'hobby':'Massage'
    },
    {
        'name':'alex',
        'hobby':'喊麦'
    },
    {
        'name':'太白',
        'hobby':'看书'
    }
]

list4 = [
    {'name':'alex','hobby_list':['抽烟','烫头','喝酒','Massage']},
    {'name':'wusir','hobby_list':['街舞','喊麦']},
    {'name':'太白','hobby_list':['看书']}
]

# 将list3这种数据类型转化成list4类型，你写的代码必须支持可扩展
# 比如list3数据在加一个这样的字典{'name':'wusir','hobby':'溜达'}
# list4 = {'name':'wusir','hobby_list':['街舞','喊麦','溜达']}
# 或者list3增加一个字典{'name':'太白','hobby':'开车'}

# 两种方式
# l1 = []
# # 1.直接构建
# for i in list3:
#     for j in l1:
#         if i['name'] == j['name']:
#             j['hobby_list'].append(i['hobby'])
#             break
#     else:
#         l1.append({'name':i['name'],'hobby_list':[i['hobby']]})
# print(l1)

# 第二种，构建特殊的数据结构
dic = {}
for i in list3:
    if i['name'] not in dic:
        dic[i['name']] = {'name':i['name'],'hobby_list':[i['hobby']]}
    else:
        dic[i['name']]['hobby_list'].append(i['hobby'])
print(list(dic.values()))
