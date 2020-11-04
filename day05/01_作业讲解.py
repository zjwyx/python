
li = ["alex","WuSir","ritian","barry","wenzhou"]
# 计算列表的长度并输出
# print(len(li));
# 列表中追加元素"seven",并输出添加后的列表
# li.append("seven");
# print(li)
# 请在列表的第一个位置插入元素"tony",并输出添加后的列表
# li.insert(0,"tony");
# print(li)
# 请修改列表第2个位置的元素为"kelly",并输出修改后的列表
# 下标改
# li[1] = "kelly"
# print(li)

# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不容许循环添加
# li.extend([1,"a",3,4,"heart"])
# print(li)
# 请将字符串s="qwert"的每个元素添加到列表li中，一行代码实现
# li.extend("qwert")
# print(li)
# 请删除列表中的元素"ritian",并输出删除后的列表
# ret = li.pop(2);
# print(ret)
# print(li)
# 请输出列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li[2])
# ret = li.pop(2)
# print(ret)
# print(li)
# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
# del li[1:]
# print(li)


# 第三天(字符串的方法)
# name = "alex leNb"
# 移除name变量对应的值两边的空格并输出处理结果(不会)
# name1 = name.replace(" ","")
# print(name1)

# 判断 name 变量是否以 "al"开头，并输出结果
# name2 = name.startswith("al");
# print(name2)

# 判断name变量是否以"Nb"结尾，并输出结果
# name3 = name.endswith("Nb");
# print(name3);

# 将name变量对应的值中的所有的"l"替换为"p"，并输出结果
# name4 = name.replace("l","p");
# print(name4)

# 将name变量对应的值中的第一个"l"替换为"p"，并输出结果
# name4 = name.replace("l","p",1);
# print(name4)

# 将name变量对应的值中的所有的"l"分割，并输出结果(分割：字符串变列表)
# name5 = name.split("l");
# print(name5)

# 将name变量对应的值根据第一个"l"分割，并输出结果
# name5 = name.split("l",1);
# print(name5)

# 将name变量对应的值变大写，并输出结果
# name6 = name.upper();
# print(name6)

# 将name变量对应的值变小写，并输出结果
# name6 = name.lower();
# print(name6)

# 字符串的切片
# s = "123a4b5c"
# 通过对s切片形成新的字符串s1,s1="123"
# s1 = s[0:3]
# print(s1)
# 通过对s切片形成新的字符串s2,s1="a4b"
# s2 = s[3:6]
# print(s2)
# 通过对s切片形成新的字符串s3,s1="1345"
# s3 = s[::2]
# print(s3)
# 通过s切片形成字符串s4，s4="2ab"
# s4 = s[1:-2:2]
# print(s4)
# 通过s切片形成字符串s5，s5="c"
# s5 = s[-1]
# print(s5)
# 通过s切片形成字符串s6，s6="ba2"
# s6 = s[-3::-2]
# print(s6)

# 使用while和for循环分别打印字符串s="asdfer"中的每个元素
# for i in "asdfer": print(i)
# 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
# for i in "asdfer": print(i)

# 使用for循环对s="asdfer"进行循环，但是每次打印的内容是每个字符串加上sb
# s="asdfer"
# for i in s:
#     print("sd" + i)

# 使用for循环对s="123"进行循环，打印的内容依次是:倒计时3,2,1，出发
# for i in "321":
#     print("倒计时"+ i + "分钟")
# 实现一个整数加法计算器：两个数相加
# 例如：content=input("请输入内容"，用户输入：3+9或3+5，然后进行分割在进行计算)
# content = input("请输入内容:");
# content1 = content.split("+");
# content2 = ",".join(content1)
# print(int(content2[0]) + int(content2[2]))

# 选做题：实现一个整数加法计算器（多个数相加）
# 例如：content=input("请输入内容"，用户输入：3+9或3+5，然后进行分割在进行计算)

# lis = [2,3,'k',['qwe',20,['k1',['tt',3,'1']],89],'ab','adv']
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)

# join() 方法  列表<======>字符串
# li = ['alex','eric','ran']
# l1 = "_".join(li)
# print(l1,type(l1))

# li = ['苍老师','东京热','武藤兰','波多野结衣']
# com_list = []
# while 1:
#     for i in li:
#         pass





li = [1,3,4,'alex',[3,7,8,'alex'],5,'RiTiAn']
# for i in li:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     else:
#         print(i)
#
for index,i in enumerate(li):
    print(index,i)