# 读并追加
f = open('文件的读写.txt',encoding='utf-8',mode='r+')
content = f.read()
print(content)
f.write('人的一切痛苦，本质都是对自己无能的愤怒')
f.close()