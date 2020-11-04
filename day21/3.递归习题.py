# 2.os模块：查看一个文件夹下的所有文件，这个文件夹下面还有文件夹
# import os
# def show_file(path):
#     name_list = os.listdir(path)
#     for name in name_list:
#         abs_path = os.path.join(path,name)
#         if os.path.isfile(abs_path):
#             print(name)
#         elif os.path.isdir(abs_path):
#             show_file(abs_path)

# show_file('F:\python')


# 4.斐波那契数列
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(3)

















