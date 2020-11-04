# callable(对象)
# 对象() 能不能运行就是callbale判断是事儿

class A:
    def __call__(self, *args, **kwargs):
        print('-------')

# obj = A()
# print(callable(obj))
# obj()
A()()
# Flask 框架的源码
