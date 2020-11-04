# 对字符串的下面两种操作，形成的都是一个新的字符串，与原来的字符串没有关系
# 第一部分：索引部分
# s1 = "python1期骑士计划"
#  通过索引取元素
# print(type(s1[0]),s1[0])
# print(s1[-2])

# 按切片取值()顾头不顾尾
# print(s1[0:6])
# print(s1[:6])
# print(s1[1:7])
# print(s1[6:-1])
# print(s1[6:-2])

# 按照切片加步长
# print(s1[0::2])
# print(s1[0:5:2])
# print(s1[1::2])
# 如果想倒序取值，加一个反向步长
# print(s1[-1:-6:-2])



# 第二部分：字符串的常用方法
# name = "oldboy"
# capitalize() 首字母大写  三星
# print(name.capitalize())

# center() 字符串居中，前后填充自定义字符  二星
# print(name.center(20,"*"))

# upper() 全部大写  lower() 全部小写     四星
# print(name.upper())
# print(name.lower())
# 应用举例:
# name = input("请输入用户名：");
# code = "ADfer";
# if code.upper() == name.upper():
#     print("登录成功")


# startswith() 判断是否以o为开头    四星
# endswith() 判断是否以y结尾
# print(name.startswith("o"))
# print(name.endswith("y"))
# print(name.startswith("l",1,5));

# swapcase() 大小写转化
# print(name.swapcase());


# s1 = "alex wusir*taibai6nvshen"
# title() 非字母隔开的每个部分首字母大写  **
# print(s1.title())

# find() 通过元素找索引 找到第一个就返回，没有此元素返回-1
# index() 通过元素找索引 找到第一个就返回，没有此元素返回-1
# print(name.find("b",1,5))                                  ???? 不懂
# print(name.index("p"))

# name = "\toldboy\n";
# name1 = "*oldboy*";
# print(name1.strip("*"))
# print(name)

# strip() 默认去除字符串前后的空格，换行符，制表符   重前，重后依次去除    五星
# print(name.strip())

# 举例:
# name = input("请输入用户名:");
# if name.strip() == "alex":
#     print("登录成功");


# s1 = "alex wusir taibai";
# s2 = ", alex, wusir, taibai";
# s3 = "alex, wusir, taibai";

#  split()     将字符串分割成列表（str ===> list）
#  默认按照空格分割
# print(s1.split());
# print(s2.split(", "))


# s5 = 'alexlwle';
# 可以设置分割次数
# print(s5.split("l",1))


# 课下自己练习的
# rsplit()

# strl = 'alex'
# join()  自定制连接符，将可迭代对象中的元素连接起来 *****
# print("*".join(strl));

# replace() 替换
#  1 是替换次数  可以设置替换次数
# str2 = 'alex 是创始人，alex很牛逼，alex...';
# print(str2.replace("alex","sb",1))


# 格式化输出 format()  三种
# s1 = '我叫{},今年{},性别{}'.format("太白","28","男")
# print(s1)

#  is系列
#  isalnum()数字或字母组成
#  isalpha()字母组成
#  isdigit()数字组成
# name = 'taobai123'
# print(name.isalnum())

# 公共方法
# count() 出现的次数
# len() 字符串的长度
name = 'alex'
print(name.count("a"))
print(len(name))


f1 = 'fdjsafjsdkla';
# while 循环
