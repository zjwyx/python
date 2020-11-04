# s1 = 'python全栈22期'

# 字符串的索引
# s2 = s1[0]
# print(s2)

# s3 = s1[-1]
# print(s3)

# 字符串的切片
# s4 = s1[0:6]
# print(s4)

#默认到最后
# s5 = s1[:6]
# print(s5)


# 字符串切片的步长
# s6 = s1[-1:-5:-1]
# print(s6)

# s7 = s1[-1::-1]
# print(s7)

# s8 = s1[:6:2]
# print(s8)

# 按索引：s1[index]
# 按照切片:s1[start_index:end_index]
# 按照切片步长 : s1[start_index:end_index:2]
# 反向按照切片步长 :s1[start_index:end_index后边一位:2]



# s = "123a4b5c"
# a.通过对s切片形成新的字符串s1 ，s1="123"
# print(s[:3])
# b.通过对s切片形成新的字符串s2 ，s2="a4b"
# s2 = s[3:6]
# print(s2)

# c.通过对s切片形成新的字符串s3 ，s3="1345"
# s3 = s[::2]
# print(s3)

# d.通过对s切片形成新的字符串s4 ，s4="2ab"
# s4 = s[1:7:2]
# print(s4)

# e.通过对s切片形成新的字符串s5 ，s5="c"
# s5 = s[-1:-2:-1]
# print(s5)

# f.通过对s切片形成新的字符串s6 ，s6="ba2"
# s6 = s[-3:0:-2]
# print(s6)


# 字符串的方法
# upper()大写 ， lower()小写
# s1 = 'taiBai'
# s2 = s1.upper()
# s3 = s1.lower()
# # print(s1)
# print(s2,type(s2))
# print(s3,type(s3))


# username = input("请输入用户名：")
# password = input("请输入密码：")
# your_code = input("请输入验证码")
# code = 'QweR'
# if your_code.upper() == code.upper():
#     if username == "xiaowei" and password == "0542":
#         print("登陆成功")
#     else:
#         print("登录失败")
# else:
#     print("验证码错误")



# startswith 以什么开头   endswith以什么结尾
# a = "dkfjdkfasf54"
# # a1 = a.startswith("jdk",3,6)
# a2 = a.endswith("54")
# print(a2)


# split 分割
# str ----- list
# s = '太白;女神;吴超'
# s1 = s.split(';')
# print(s1,type(s1))

# s = ';太白;女神;吴超'
# s1 = s.split(';')
# print(s1)


# join  非常重要
# list ---  str
# s1 = ["太白","女神","吴超"]
# s2 = ";".join(s1)
# print(s2,type(s2))


# replace 替换
# s = 'xiaowei很漂亮，xiaowei很仔细，xiaowei是一个不错的姑娘'
# s1 = s.replace("xiaowei","小魏")
# print(s1)

# format 格式化输出
# 第一种用法
# s = "我叫{0}，今年{1}，性别{2}".format("赵健",25,"男")
# print(s)
# 第二种用法
# s = "我叫{}，今年{}，性别{}".format("赵健",25,"男")
# print(s)
# 第三种用法
# s = "我叫{name}，今年{age}，性别{sex}".format(name="赵健",age=25,sex="男")
# print(s)


#is系列
# name='taibai123'
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
# print(name.isdecimal()) #字符串只由十进制组成





# split 方法 和 join 方法 复习
# split方法  str ----- list
# s = "太白;女神;吴超"
# s1 = s.split(";")
# print(s1)

# join 方法
# list ---- str
# s = ["太白","女神","吴超"]
# s1 = ";".join(s)
# print(s1)