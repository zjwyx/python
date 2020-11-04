# def func1():
#     name = '张三'
#
#     def func2(arg):
#         print(arg)
#
#     func2(name)
#
# func1()

# 灵魂三问2
def func1():
    name = '夏宇航'
    def func2():
        # 内层函数的作用域里没有name，会自动往外层函数的作用域去找
        print(name)
    func2()
func1()

# 灵魂三问3
def func1(name):

    def func2():
        # 内层函数的作用域里没有name，会自动往外层函数的作用域去找
        print(name)
    func2()
func1('夏宇航')








































