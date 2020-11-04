class Foo:
    def __init__(self,num):
        self.num = num

# v1 = [Foo for i in range(10)]
# v2 = [Foo(5) for i in range(10)]
# v3 = [Foo(i) for i in range(10)]
#
#
# print(v1)
# print(v2)
# print(v3)


# obj1 = Foo(10)
# print(obj1)
# obj2 = Foo(10)
# print(obj2)




class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 两个对象作比较的时候会自动调用这个方法
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

    def __gt__(self, other):
        print('执行gt方法')
    def __lt__(self, other):
        print('执行lt方法')


alex = Person('alex',84)
alex222 = Person('alex',84)

# == 符号刚好会调用alex对象的类的__eq__方法，alex22会被当做other参数传入方法
# alex == alex222的结果就是__eq__方法的返回值
print(alex == alex222)




