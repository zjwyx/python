'''
测试相对导入
'''

import sys
import os

# 把项目所在的父路径添加到sys.path中
sys.path.append(os.path.dirname(__file__))

from xx.y import yy

print(yy.age2)

print(yy.age)
yy.f()