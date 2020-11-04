# 创建数组的第一种方法
# l1 = ["太白","alex","女神","吴超"]

# 创建的第二种方法(不常用)
# l1 = list("fjajdjdka")
# print(l1)


# 增 append()
# l1 = ["太白","alex","女神","吴超"]
# while 1:
#     name = input("请输入姓名：")
#     if name.upper() == "Q":
#         break
#     l1.append(name)
#
# print(l1)

# insert 插入在列表的任意位置插入元素
# l1 = ["太白","alex","女神","吴超"]
# l1.insert(3,"wusert");
# print(l1)

# extend 迭代着追加，在列表的最后面迭代着追加一组数据
# l1 = ["太白","alex","女神","吴超"]
# # l1.extend("abcdefg");
# l1.extend(["一万","二筒"])
# print(l1)

# 删
# remove 通过元素删除列表中该元素
# l1 = ["太白","alex","女神","吴超"]
# l1.remove("太白")
# print(l1)

# pop 通过索引删除
# l1 = ["太白","alex","女神","吴超"]
# l1.pop(-1)
# print(l1)

# del 删除
#   按照索引删除
# l1 = ["太白","alex","女神","吴超"]
# del l1[-1]
# print(l1)
#   切片删除元素
# l1 = ["太白","alex","女神","吴超"]
# del l1[1:]
# print(l1)
#   切片（步长）删除元素
# l1 = ["太白","alex","女神","吴超"]
# del l1[::2]
# print(l1)
# clear  清空
# l1 = ["太白","alex","女神","吴超"]
# l1.clear()
# print(l1)

# 改
#   按照索引
# l1 = ["太白","alex","女神","吴超"]
# l1[0] = "老男孩"
# print(l1)

#   按照切片
# l1 = ["太白","alex","女神","吴超"]
# l1[1:3] = 'abcdefg'
# print(l1)

#   按照切片(步长)，必须一一对应
# l1 = ["太白","alex","女神","吴超"]
# # l1[::2] = ["一筒","三万"]
# l1[::2] = "一筒"
# print(l1)

# 查
# l1 = ["太白","alex","女神","吴超"]
# for i in l1:
#     print(i)