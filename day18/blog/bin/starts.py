'''
启动文件
'''

# import src
# 直接引用不到，他不在内存，内置，在sys.path

# 这么做虽然实现了，但是有问题
# 1.项目中的这些py文件，肯定会互相引用，src 引用 settings，src引用comment.py
# import sys
# # 列表
# sys.path.append(r'F:\python学习\day18\blog\core')
# import src
# src.run()


# ****************************
# import sys
# # 列表,直接添加blog的目录
# sys.path.append(r'F:\python学习\day18\blog\core')
# sys.path.append(r'F:\python学习\day18\blog\db')
# sys.path.append(r'F:\python学习\day18\blog\lib')
# from core import src
# # import src
# # src.run()





# import sys
# # 列表,直接添加blog的目录
# sys.path.append(r'F:\python学习\day18\blog')
# from core import src
# import src
# src.run()

'''
# 问题2：此项目 在我的计算机中，他的路径F:\python学习\day18\blog 写死了
# 动态的获取blog的路径，无论再谁的计算机中，都可以找到blog的绝对路径
import sys
# 列表,直接添加blog的目录
sys.path.append(r'F:\python学习\day18\blog') 
from core import src
import src
src.run()

'''

# import sys
# import os
# 动态获取本文件的绝对路径
# print(__file__)
# # 动态的获取父级的目录
# print(os.path.dirname(__file__))
# # 动态获取爷爷级
# print(os.path.dirname(os.path.dirname(__file__)))


# ************以上都是思路********************

import sys
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from core import src

if __name__ == '__main__':
    src.run()



























