'''
l1 = [3,2]
l1 += [5]
结果[3,2,5]

'''

import copy
# v1 = [1,2,3,4]
# v2 = copy.copy(v1);
# print(v2)
# v3 = copy.deepcopy(v1)
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])

# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1);
# v3 = copy.deepcopy(v1)
# print(v1[-1] is v2[-1])
# print(v1[-1] is v3[-1])
# print(v2[-1] is v3[-1])


# 需要理解（没做了）
# v1 = [1,2,3,{'name':'太白','numbers':[7,77,88]},4,5]
# v2 = copy.deepcopy(v1);
#
# print(v1 is v2)
# # false
# print(v1[0] is v2[0])
# # true
# print(v1[3]['name'] is v2[3]['name'])
# # true
# print(v1[3]['numbers'] is v2[3]['numbers'])
# # false
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# # true




# l1 = []
# for i in range(3):
#     l1.append(["_"]*3)
# print(l1)


# 列表的坑
# 第一：把它添加到一个新的列表，在删除
# 第二：倒序删
# 第三：切片（行不动）
# lst = ['钱老二','钱星星',"马化腾","钱扒皮"];
# 倒序的方法

# new_list = []
# for line in lst:
#     # print(line)
#     if '钱' in line:
#         new_list.append(line)
# # 数组
# print(new_list)
# # 循环数组
# for aaa in new_list:
#     lst.remove(aaa)
# print(lst)


# 水仙花数
# num = int(input("请输入三位数:"));
#
# gewei = int(num % 10)
# shiwei = int((num / 10) % 10)
# baiwei = int(num / 100)
# if gewei ** 3 + shiwei ** 3 + baiwei ** 3 == num:
#     print('水仙花数为',num)
# else:
#     print("这不是水仙花数")


# 车牌区域划分，现给出以下车牌，根据车牌的信息，分析出各省的车牌持有量
cars = ['鲁A3244','鲁B12333','京B8989M','黑C46556','沪B25041']
locals = {'沪':'上海','黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南','京':'北京'}
# 结果：{'黑龙江':2,'山东':1,'北京':1}
# 循环遍历的主题：carse
# 在循环中给字典添加键值对
# dic = {}
# for i in cars:
#     # print(locals[i[0]])
#     if locals[i[0]] not in dic:
#         dic[locals[i[0]]] = 1
#     else:
#         dic[locals[i[0]]] = dic[locals[i[0]]] + 1
# print(dic)

# dic = {}
# for i in cars:
#     dic[locals[i[0]]] = dic.get(locals[i[0]],0) + 1
#
# print(dic)







