# print('from the tbjx.py')
# 配合*使用
__all__ = ['name','read1']

name = '太白金星'

def read1():
    print('tbjx模块',name)

def read2():
    print('tbjx模块')
    read1()


def change():
    global name
    name = 'barry'
    print(name)

# 测试代码
# change()
if __name__ == '__main__':
    change()


# print(__name__)
# 当tbjx做脚本的时候:__name__ == __main__返回True
# 当tbjx做模块被别人引用的时候:__name__ == tbjx
#
# __name__根据文件的扮演的角色（脚本，模块）不同而得到不同的结果
# 1.模块需要调试时，加上if __name__ == '__main__':
# 2.作为项目的启动文件，需要用
import time

# print(666)
# print(name)
# change()
# print(name)