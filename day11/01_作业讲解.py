# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)

# 集合，返回一个元组（说明是位置参数）
# func(*{'无佩奇','金星','女神'})



# def func(name,age=19,email='123@qq.com'):
#     print(name)
#     print(age)
#     print(email)
# func('alex',20)
# func('alex',20,30)

# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)
# c = test5(b, a)
# print(c)


a = 10
b = 20
def test5(a, b):
    a = 20
    b = 10
    a = 3
    b = 5
    print(a, b)
c = test5(b, a)
print(c)