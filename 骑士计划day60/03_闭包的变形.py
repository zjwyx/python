# def func1(name):
#     def func2():
#         print(name)
#
#     return func2
#
# # 内层函数+其外层函数变量的引用
# ret = func1('夏宇航')
# ret()


def func1():
    def func2():
        def func3():
            def func4():
                print('嘿嘿')
            return func4
        return func3
    return func2

ret1 = func1()
ret2 = ret1()
ret3 = ret2()
ret3()






