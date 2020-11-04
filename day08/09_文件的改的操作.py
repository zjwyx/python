'''
1.以读的模式打开原文件
2.以写的模式创建一个新文件
3.将原文件的内容读出来修改成新内容，写入新文件
4.将原文件删除
5.将新文件重命名为原文件
'''

import os
#1.以读的模式打开原文件
# 2.以写的模式创建一个新文件
# with open('alex自述',encoding='utf-8',mode='r') as f1,\
#         open('alex自述.bak',encoding='utf-8',mode='w') as f2:
#     old_content = f1.read()
#     new_content = old_content.replace('alex','SB');
#     f2.write(new_content)
# os.remove('alex自述')
# os.rename('alex自述.bak','alex自述')


# 进阶版
with open('alex自述',encoding='utf-8',mode='r') as f1,\
    open('alex自述.bak',encoding='utf-8',mode='w') as f2:
    for line in f1:
        line = line.replace('SB','alex')
        f2.write(line)
os.remove('alex自述');
os.rename('alex自述.bak','alex自述')
# 有关清空的问题
# 关闭文件句柄，再次以w模式打开此文件时，才会清空