'''
自定义模块
模块中出现的变量，for循环，if结构，函数的定义....称为模块的成员
'''

# 可执行语句
a = 1
# print(a)


# for i in range(3):
#     print(i)


# 函数定义，不可执行
def f():
    print('hell word')

# f()


# __name__:脚本方式运行时，固定的字符串：__name__
# 以导入方式运行，就是本模块的名字
# print(__name__)


# 定义一个函数，包含测试语句
def main():
    print(a)
    for i in range(3):
        print(i)
    f()


# 开发阶段
if __name__ == '__main__':
    main()
























































































































































