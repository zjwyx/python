#寻找字符串中的元素是否存在
# ret6 = a4.find("fjdk",1,6)
# print(ret6)  # 返回的找到的元素的索引，如果找不到返回-1

# ret61 = a4.index("fjdk",4,6)
# print(ret61) # 返回的找到的元素的索引，找不到报错。

# **************************************************************************************************

# str 补充的方法练习一遍就行
# name = "taiBAi";
# capitalize() 首字母大写,其余变小写
# print(name.capitalize());
# swapcase()  大小写翻转
# print(name.swapcase())
# msg='taibai say hi';
# title() 每个单词的首字母大写
# print(msg.title())
# sl = "barry"
# center() 居中
# print(sl.center(20,'*'))

# find 通过元素找索引，找到第一个返回，找不到返回-1
# index 通过元素找索引，找到第一个返回，找不到则报错
# print(sl.find('a'))
# print(sl.index("p"))

# tupe
# 元祖中如果只有一个元素，并且没有逗号，那么他不是元组，他与改元素的数据类型是一致的  ***
# tul = ("太白")
# print(tul,type(tul))
# tul = (1,)
# print(tul,type(tul))

# cont() 出现的次数
# tul = (1,2,3,3,3,4,5,6,6)
# print(tul.count(3))
# index()
# tul = ("太白","alex","太白")
# print(tul.index("太白"))


# list
# l1 = ["太白","123","女神","大壮"]
# count pass
# index
# print(l1.index("大壮"))
# sort  从小到大
# l2 = [5,4,3,7,8,6,1,9]
# l2.sort()
# sort(reverse=True) 从大到小
# l2.sort(reverse=True)
# reverse() 翻转
# l2.reverse()
# print(l2)

# 列表可以相加（重要）
# l1 = [1,2,3]
# l2 = ["太白","女神","123",2]
# print(l1 + l2)

# 列表与数字相乘
# l1 = [1,2,3]
# print(l1 * 3)

# l1 = [11, 22, 33, 44, 55]
# 索引为奇数，我就删除
# range() 里面是数的范围
# enumerate() 可以设置索引

# for key,i in enumerate(l1,0):
#     if key % 2 != 0:
#         l1.pop(key);
# print(l1)

# 列表的特性：
# 最简答的
# del l1[1::2]
# print(l1)

# 倒序法删除元素
# for i in range(len(l1)-1,-1,-1):
#     if i % 2 != 0:
#         l1.pop(i)
# print(l1)

# 思维置换
# l1 = [11, 22, 33, 44, 55]
# new_lis = []
# for i in range(len(l1)):
#     if i % 2 == 0:
#         new_lis.append(l1[i])
# print(new_lis)

# 循环一个列表时，最好不要改变列表的大小，这样会影响你的最终结果


# dict
# 字典的补充
# update() 增改更新
# dic = {"name":"alex","age":23}
# dic.update(hobby = "运动",height="178")
# dic.update(name = "alexsb")
# 面试考
# dic.update([(1,'a'),(2,'b')])
# print(dic)


# dic1 = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic1.update(dic2)
# print(dic1) # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
# print(dic2) # {'name': 'alex', 'weight': 75}

# fromkeys() 值共有一个，面试题，共用一个
# dic = dict.fromkeys([1,2,3],'alex')
# print(dic)
dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}

# for i in dic:
#     if 'k' in i:
#         del dic[i]
# print(dic)

# 你会发现，报错了。。。。。
# 错误原因：
# RuntimeError: dictionary changed size during iteration
# 翻译过来是：字典在循环迭代时，改变了大小。

# 循环一个字典时，如果改变这个字典的大小，就会报错
# l1 = [];
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# print(l1)
# for i in l1:
#     dic.pop(i)
# print(dic)

# for i in list(dic.keys()):
#     if 'k' in i:
#         dic.pop(i)
# print(dic)

# 0,'',(),[],{},set(), None

# 数据类型的转化
# int str bool 三者转化
# str <======> bytes
# str <======> list   strip()(重中之重)
# list <=====> str    join() 此list中的元素全部都是str类型
# dict.keys()  dict.values()  dict.items    list()
# s1 = "alex wusir taibai"
# l1 = s1.split(" ")
# print(l1)

# tuple <====> list
# dict =====> list