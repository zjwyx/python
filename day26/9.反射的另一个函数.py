class A:
    Role = '治疗'
    def __init__(self):
        self.name = 'alex'
        self.age = 84

    def func(self):
        print('wahaha')
        return 666
a = A()
# print(hasattr(a,'sex'))
# print(getattr(a,'age'))
# print(getattr(a,'func'))

if hasattr(a,'func'):
    if callable(a,'func'):
        getattr(a,'func')()
# print(callable(a.func))
# print(callable(a.name))







































