'''
配置文件 register_path静态的路径
数据库连接设置，变量不要改变值能引用
'''

import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))


register_path = os.path.join(BASE_PATH,'db','register')

