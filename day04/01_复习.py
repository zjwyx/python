# s = "123a4b5c"
# # 2.有字符串s = "123a4b5c"
# # 通过对s切片形成新的字符串s1,s1="123"
# s1 = s[:3]
# print(s1)
# # 通过对s切片形成新的字符串s2,s2="a4b"
# s2 = s[3:6]
# print(s2)
# # 通过对s切片形成新的字符串s3,s3="1345"
# s3 = s[::2]
# print(s3)
# # 通过对s切片形成新的字符串s4,s4="2ab"
# s4 = s[1:6:2]
# print(s4)
# # 通过对s切片形成新的字符串s5,s5="c"
# s5 = s[-1]
# print(s5)
# # 通过对s切片形成新的字符串s6,s6="ba2"
# s6 = s[-3:-8:-2]
# print(s6)

# 使用while和for循环分别打印字符串s="asdfer"中的每个元素
# for i in 'asdfer':
#     print(i)


# 使用for循环对s="asdfer"进行循环，每次打印的内容是每个字符加上sd
# s = "asdfer"
# for i in s:
#     print(i + 'sd')



# 使用for循环对s=“123”进行循环，打印的内容依次是："倒计时3秒","倒计时2秒","倒计时1秒"
# s = "321"
# for i in s:
#     # print("倒计时"+i+"秒")
#     print("倒计时{}秒".format(i))



# split 方法
# s = "太白 女神 吴超"
# s1 = s.split()
# print(s1)

# join方法
# s = ["小魏","赵健","魏雅昕"]
# s1 = ';'.join(s)
# print(s1)

# 字符串的常用方法
# s = " 123a4b5c"
# 替换 大写 小写 以什么结尾 以什么开头 格式化输出 is系列 去除空格
# replace() endswith() startswith
# s.replace()
# s.upper()
# s.lower()
# s.endswith()
# s.startswith()
# s.format()
# s.isalnum()
# s.strip()

s = "我叫{0}，我的名字{1}，性别{2}，我行不改名坐不改姓,还叫{0}".format("赵健",25,"男")
print(s)



















