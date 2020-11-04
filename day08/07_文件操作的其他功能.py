# tell 读取光标的位置，单位字节
# f = open('文件的读写.txt',encoding='utf-8',mode='r+')
# print(f.tell())
# content = f.read()
# print(f.tell())
# # print(content)
# f.close()

# seek 调整光标的位置
# f = open('文件的读写.txt',encoding='utf-8')
# f.seek(6)
# content = f.read()
# print(content)
# f.close()

# flush 强制刷新
f = open('文件的其他功能',encoding='utf-8',mode='w')
f.write('jdsaklfjdkasljfi')
f.flush()
f.close()