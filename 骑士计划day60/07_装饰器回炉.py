def create_people():
    print('女娲娘娘真厉害，抓把泥捏一下吹口气，就成了人')

# 按照闭包的格式写了一个函数
def a(func):
    def b():
        print('加把水')
        func()
    return b

create_people = a(create_people)
create_people()


# 1.先计算等号右边的a(create_people)
# 2.create_people = b
# 3.create_people() ==> b()
# 4.b是一个闭包，会引用a函数的func，func-->指向原来的create_people



































