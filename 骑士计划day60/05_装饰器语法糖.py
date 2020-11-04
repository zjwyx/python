

def a(func):
    def b():
        print('加点水')
        func()
    return b

# 相当于把被装饰的函数当成参数传给a，然后把返回值在赋值给被装饰的函数名
@a
def create_people():
    print('女娲娘娘真厉害，抓把泥捏一下吹口气，就成了人')

@a
def create_pig():
    print('女娲娘娘真厉害，捏了一个猪')

# 相当于调用了内层函数b
create_people()







