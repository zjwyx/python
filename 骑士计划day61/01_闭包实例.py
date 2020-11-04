def f1(name):

    def f2():
        print('hell',name)
    return f2

ret = f1('阿玟')
ret()
del f1
ret()
