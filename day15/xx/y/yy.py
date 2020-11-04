'''
次模块作为对外引用的入口
'''

# 相对导入同项目下的模块
# 这样容易向外暴露zz模块
# from ..z import zz

from ..z.zz import *

# 定义自己的成员
age2 = 888
def f2():
    print('f2')
