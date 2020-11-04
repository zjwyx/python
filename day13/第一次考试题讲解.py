# l1 = list('abcde')
# print(l1[10:])
# print(l1[10])

# import copy
#
# a = [1,2,3,[4,5],6]
# b = a
# c = copy.copy(a)
#
# d = copy.deepcopy(a)
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a)
# # [1,2,3,[4,5,11],6,10]
# print(b)
# # [1,2,3,[4,5,11],6,10]
# print(c)
# # [1,2,3,[4,5,11],6]
# print(d)
# # [1,2,3,[4,5,12],6]



# 循环一个列表，最好不要改变大小
# 循环一个列表，实际上是按照索引循环的（坑）
alist = [2,4,5,6,7]
for var in alist:
    if var % 2 == 0:
        alist.remove(var)
print(alist)

