
# dic = {
#     '太白':{'name':'太白金星','age':18,'sex':'男'},
#     'python22期':['主管梁','大壮']
# }
# 键必须是不可变的数据类型 int str
# 值可以是任意数据类型，对象
# 字典在3.5之前时无序的
# 字典在3.6版本初建字典的顺序排列
# 字典的优点：查询速度非常快，存储关联型的数据
# 字典的缺点：以空间换时间
# 字典的创建方式

# 方式一：
# dic = dict((('one',1),('two',2),('three',3)))
# print(dic)

#  方法二：
# dic = dict(one = 1,two=2,three=3)
# print(dic)

#  方法三：
# dic = dict({"one":1,"two":2,"three":3})
# print(dic)

#  增删改查
dic = {"name":"太白","age":18,"hobby_list":['直男',"开车"]}
#  增
# 直接增加，键是唯一的
# 有则改之，无则增加
# dic["sex"] = "男";
# print(dic)

# setdefault()
# 有则不变，无则增加
# dic.setdefault("hoddy","打游戏")
# print(dic)

# update() 增    里面的参数是字典，有则改之无则增加

# 删
# pop() 按照键删除键值对  有返回值   ***
# 设置第二个参数则无论字典中有无此键都不会报错
# dic.pop('age')
# print(dic)
# ret = dic.pop('hoddy','没有此键')
# print(ret)
# print(dic)

#  clear() 清空
# dic.clear();
# print(dic)

# del()
# del dic["age"]
# print(dic)


# 改
# dic['name'] = "alex"
# print(dic)

# 查
# print(dic['hobby_list'])

# get()  ***
# li = dic.get('hobby_list');
# print(li)

#  三个特殊的
# keys() values() items()
# print(dic.keys())
# 可以转化成列表
# print(list(dic.keys()))
# for key in dic.keys():
#     print(key)

# values()
# print(dic.values())

# items() 所有的键值对
# print(dic.items())
# for i in dic.items():
#     print(i)

# 元祖的拆包
# a,b = ("name","太白")
# print(a,b)

# 面试题
# a = 18
# b = 12
# a,b = b,a
# print(a,b)


dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"] = "v4"
# print(dic)
# dic.setdefault("k4","v4");
# print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(444);
# print(dic)

# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(1,18);
print(dic)