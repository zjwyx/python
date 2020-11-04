# 多个装饰器装饰同一个函数

def foo1(func):
    print('d1')

    def inner1():
        print('inner')
        return '<i>{}</i>'.format(func())
    return inner1

def foo2(func):
    print('d2')

    def inner2():
        print('inner2')
        return '<b>{}</b>'.format(func())
    return inner2

@foo1
@foo2
def f1():
    return 'Hell Andy'

ret = f1()
print(ret)
# f1 = foo2(f1)  --> inner2
# f1 = foo1(inner2)
# f1()  --> inner()
