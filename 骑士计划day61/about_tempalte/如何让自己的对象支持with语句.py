'''
如何让自己创建的类对象支持with语句
with：上下文管理器协议
什么场景使用
    网络连接，数据库连接，文件句柄，用到锁
'''


class A:
    def __enter__(self):
        print('进入with语句块自动执行该方法')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出with语句块，自动执行该方法')

with A() as f:
    print('嘿嘿')
    print(f)
print('在来一次')

# pymysql模块
