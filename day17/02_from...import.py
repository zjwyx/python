# from tbjx import name
# from tbjx import read1
# from tbjx import read2
# # print(name)
# print(globals())

# 1.容易产生冲突，后者将前者覆盖
# name = 'alex'
# from tbjx import name
# print(name)


# from tbjx import read1

# def read1():
#     print(666)
# name = '大壮'
# read1()


# from tbjx import change
# name = 'alex'
# # alex
# print(name)
# # barry
# change()
# # alex
# print(name)


# from tbjx import *
# # 一般千万别这样写，必须要将这个模块中的所有名字都记住
# # 但是可以配合一个变量使用
# print(name)
# read1()
# # read2()


# from tbjx import read2
# read2()


# import tbjx



# 模块的搜索路径：
# import tbjx
# print(tbjx.name)

# import dz
# print(dz.name)

# 搜索路径
# import sm
# python 解释器会自动将一些内置内容（内置函数，内置模块等）模块加载到内存中
import sys
# print(sys.modules)
# 第一个参数：路径是当前执行文件的相对路径
print(sys.path)


# 我就想找到dz，内存没有，内置中，这两个你是行不通的，sys.path你可以操作

import sys
sys.path.append(r'F:\python学习\day16')
# sys.path 会自动将你的 当前目录的路径加载到列表中
import dz

# 如果你想要引用你自定义的模块
# 要不你将这个模块放到当前目录下面，要不你就手动添加到sys.path
