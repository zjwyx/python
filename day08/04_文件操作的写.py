# 没有文件，创建文件，写入内容
# f = open('文件的写',encoding='utf-8',mode='w');
# f.write('随便写一点东西');
# f.close();


# 如果文件存在，先清空源文件内容，在写入新内容
# f = open('文件的写',encoding='utf-8',mode='w');
# f.write('太白真丑.....');
# f.close();

# wb 非文本类型的文件
f = open('1.jpg',mode='rb');
content = f.read()
# print(content)
# f.close()

f = open('美女2.jpg',mode='wb')
f.write(content)
f.close()