# read()
# f = open('今日内容大纲.txt',mode='r',encoding='utf-8')
# content = f.read()
# print(content)
# print(content)
# f.close()

# read(n)  n按照字符读取
# f = open('今日内容大纲.txt',mode='r',encoding='utf-8')
# content1 = f.read(4)
# print(content1)
# f.close()

# readline()  每次只读取一行
# 注意点:readline()读取出来的数据在后面都有一个\n    (换行)
# 为了去除字符串中的空格，制表符等，后面加.strip()即可
# f = open('今日内容大纲.txt',mode='r',encoding='utf-8')
# content = f.readline().strip()
# content1 = f.readline().strip()
# content2 = f.readline().strip()
# print(content)
# print(content1)
# print(content2)
# f.close()

#  readlines()
#  返回一个列表，列表里面每个元素是原文件的每一行，如果文件很大，占内存，容易崩盘。

# for循环
# f = open('alex自述',encoding='utf-8',mode='r');
# for i in f:
#     print(i.strip())

# print(f.readline())

# rb模式
f = open('1.jpg',mode='rb');
content = f.read()
print(content)
f.close()