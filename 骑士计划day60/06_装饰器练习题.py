def wrapper(func):
    def inner():
        print('夏宇航')
        func()
        print('元曾铭')
    return inner


@wrapper
def func1():
    print('永远不要高估自己')

func1()

