'''
测试自定义模块的导入
'''

# 使用阶段


# 自定义模块被其他模块导入时，其中的可执行语句会立即执行
# import a
# import time

# 查看sys.path的内容
# import sys
# print(sys.path)

# 使用os模块获取一个路径的父路径
# import os
# print(os.path.dirname(__file__)+'/aa')
# # 添加a.py所在的路径到sys.path中
# # import sys
# # sys.path.append(r'F:\python学习\day15\aa')
#
# # 使用相对位置找到aa文件夹
# # 当前文件的绝对路径
# print(__file__)


# sys 是一个列表
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/aa')


import a
print(a.a)
a.f()

# print(time.time())
# 使用自定义模块的成员
# print(a.a)
# a.f()


# python 中提供一种可以判断自定义模块属于开发阶段还是使用阶段

































































































