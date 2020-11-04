# 元组:只读列表，只允许查询，不允许增删改
tul = ("alex",100,True,[1,2,3],{'name':'太白'},(2,3))
# 索引，切片，切片+步长
# print(tul[0])
# print(tul[:3])

# for i in tul:
#     print(i)

# print(tul.index("alex"))

# 应用场景：一些非常重要的数据，不允许所有人修改的，放在元祖中
# 元祖 儿子不能改，孙子可能可以改