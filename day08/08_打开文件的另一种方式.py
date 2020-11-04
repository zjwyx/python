# 优点一：不用手动关闭文件句柄
# with open('文件的其他功能',encoding='utf-8') as f1:
#     print(f1.read())



# 优点2：
with open('文件的其他功能',encoding='utf-8') as f1,\
        open('文件的写',encoding='utf-8',mode='w') as f2:
    print(f1.read())
    for i in f1:
        print(i)
    # f2.write('akfjkdahjf')


# 缺点： 待续