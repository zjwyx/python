'''
os 和操作系统相关的操作被封装到这个模块中
'''

import os

# 和文件操作相关，重命名，删除
# os.remove('a.txt')

# os.rename('a.txt','b.txt')

# 删除目录，必须是空目录
# os.removedirs('aa')

# 使用shutil模块可以删除带内容目录
# import shutil
# shutil.rmtree('aa')

# 和路径相关的操作，被封装到另外一个os.path
# 不判断路径是否存在
# res = os.path.dirname(r'd:/aa/bbb/ccc/a.txt')
# print(res)


# 获取文件名
# res = os.path.basename(r'd:/aa/bbb/ccc/a.txt')
# print(res)

# 把路径中的路径名和文件名划分开，结果是元组
# res = os.path.split(r'd:/aa/bbb/ccc/a.txt')
# print(res)

# 合并路径
# res = os.path.join(r'd:/aa/bbb/ccc', 'a.txt')
# print(res)

# 如果是/开头的路径，默认是在当前盘符下
# res = os.path.abspath(r'd:/a/b/c')
# print(res)


# 判断

# res = os.path.isabs(r'd:/a.txt')
# print(res)
#
# res = os.path.isabs('a.txt')
# print(res)

# 文件不存在返回false，存在true
# res = os.path.isdir(r'd:/a.txt')
# print(res)

# res = os.path.exists(r'd:/a.txt')
# print(res)

# res = os.path.exists(r'd:/a.txt')
# print(res)

# 文件不存在返回false，存在true
# res = os.path.isfile(r'd:/a11.txt')
# print(res)



























