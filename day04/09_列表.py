# 列表：python基础数据类型之一。其他语言中也有列表的概念，js中叫数组,可索引，可切片，可加步长
# li = ["alex",100,True,[1,2,3],{'name':'太白'},(2,3)];

#  1.索引，切片，切片+步长
# print(li[0],type(li[0]))
# print(li[1],type(li[1]))
# print(li[2],type(li[2]))
# print(li[0:4],type(li[0:4]))
# print(li[0::2])



l1 = ["alex","wusir","taibao","egon","nvshen","温州","日天"]
#  2.增删改查，其他方法
# 增
# append  追加
# l1.append("小文");
# l1.append([1,2,3]);
# print(l1)

# insert() 插入
# l1.insert(1,"baoyuan");
# print(l1)

# extend() 迭代着追加
# l1.extend("abc")
# l1.extend([111,222,333]);
# print(l1)


# 删除
# remove() 按照元素删除
# l1.remove("alex");
# print(l1)

# pop() 按照索引删除,有返回值
# l1.pop(0);
# print(l1.pop(0))
# print(l1);

#  clear()清空
# l1.clear()
# print(l1)

# del
# 可以按照索引删除
# del l1[0]
# print(l1)
# 可以按照切片删除（可以加步长）
# del l1[0:2]
# print(l1)
# del l1[1::2]
# print(l1)
# 可以在内存级别删除列表
# del l1
# print(l1)


# 改
# 按照索引改
# l1[0] = 'aaa'
# print(l1)

# 按照切片（加步长）  跟extend()相似
# l1[0:2] = "abc"
# l1[0:2] = ["aaa","bbb","ccc"]
# print(l1)

# 加步长（一一对应）
# l1[:3:2] = "af"
# print(l1)

#  查
# 索引 切片 切片+步长
# for循环

# 其他方法
# len() 查询个数
# print(len(l1))
# 查询出现的个数
# print(l1.count("alex"))
# print(l1.index("alex"))

# sort() 从小到大排序
# sort(reverse=True) 从大到小


#  3.列表的嵌套
l3 = ['alex','wusir',['taibai',9,"ritina"],20]

# 1.找到alex的e元素
s1 = l3[0]
print(s1.index("e"))
# 2.将wusir变成大写
s2 = l3[1]
print(s2.upper())
# 3.给此列表['taibai',9,"ritina"]追加一个文州
s3 = l3[2];
print(s3)
s3.append("文州")
print(s3)
# 4.将'taibai'首字母大写
s4 = l3[2][0]
print(s4.capitalize())
# 5.将99通过数组加1的方式变成100，并放回到原处