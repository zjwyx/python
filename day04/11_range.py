
# range:自定制的 数字范围的 列表  可迭代对象类比成列表
# range(1,101)
# print(range(1,101))

# range() 一般和for循环结合使用

# for i in range(1,11):
#     print(i);

# for i in range(10,1,-1):
#     print(i)

l1 = ["alex","wusir","taibao","egon","nvshen","温州","日天"]
# 方法1：不好
# for i in l1:
#     print(l1.index(i))
# for i in range(len(l1)):
#     print(i)

#  in 判断元素在不在列表里面
# print("alex" in l1)