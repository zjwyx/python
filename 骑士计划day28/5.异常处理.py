# 异常处理
# 异常
    # 在编译阶段没问题，在执行阶段才报错
# 语法错误：在程序之前就规避掉，不应该留到程序中来进行异常处理
    # 编译，执行
    # 编译的过程中报错
    # if name = 1：
    #     pass


# 异常出现之后的现象：程序就不继续执行了

# 如何来查看异常


# 万能异常
try:
    open('aaa')
except Exception as e:
    print(e)
