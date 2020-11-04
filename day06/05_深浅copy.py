# 赋值运算
# l1 = [1,2,3,[22,33]]
# l2 = l1
# l1.append(666)
# print(l1)
# print(l2)

# 浅copy
# l1 = [1,2,3,[22,33]]
# l2 = l1.copy()
# l1.append(666)
# print(l1,id(l1))
# print(l2,id(l2))


l1 = [1,2,3,[22,33]]
l2 = l1.copy()
l1[-1].append(666);
print(id(l1[-1]))
print(id(l2[-1]))
print(l1,id(l1))
print(l2,id(l2))

# 深拷贝
# import copy
# l1 = [1,2,3,[22,33]]
# l2 = copy.deepcopy(l1)
# l1[-1].append(666)
# print(l1)
# print(l2)

# 面试必考
# 切片是浅copy
l1 = [1,2,3,[22,33]]
l2 = l1[:]
l1[-1].append(666)
print(l1)
print(l2)
# 浅copy：list dict ：嵌套的可变的数据类型是同一个
# 深copy：list dict ：嵌套的可变的数据类型不是同一个

# 今日总结
# id is == 三个方法要会用，知道是作什么的
# 集合：列表去重，关系测试
# 深浅copy:理解浅copy，深浅copy，课上练习整明白

# 预习内容
