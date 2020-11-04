# def create_people():
#     print('女娲娘娘真厉害，抓把泥捏一下吹口气，就成了人')
#
# create_people()

# 三年大旱


# def create_people():
#     print('加点水')
#     print('女娲娘娘真厉害，抓把泥捏一下吹口气，就成了人')
#

# def crate_people_with_water():
#     print('加点水')
#     create_people()


# 既不想修改原来的函数，也不想修改函数的调用方式

def create_people():
    print('加点水')
    print('女娲娘娘真厉害，抓把泥捏一下吹口气，就成了人')


def a(func):
    def b():
        print('加点水')
        func()
    return b

# 内层的b函数
# ret = a(create_people)
# ret()

# 内层的b函数，引用了func，func--->create_people
create_people = a(create_people)
# 相当于调用了内层函数b
create_people()
































