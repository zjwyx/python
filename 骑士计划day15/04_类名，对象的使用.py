
# 一个公共框架，一个公共模型
# class Person:
#     # 静态属性（共有的）
#     animal='高级动物'
#     walk_way='直立行走'
#     language='语言'
#
#     # 方法(相关的)
#     def eat(self):
#         print('该吃吃，该喝喝，啥事别忘心里搁')
#
#     def work(self):
#         print('人类都需要工作...')

# 类名
#   1.查看类中的所有属性和方法__dict__
# print(Person.__dict__)
# 通过__dict__方式，单独的属性及方法可以查但是不能增删改查
# print(Person.__dict__['animal'])
# Person.__dict__['animal'] = '低级动物'
# Person.__dict__['name'] = 'alex'
# print(Person.__dict__)

# 工作中，学习中，一般用到__dict__查看类中的所有属性及方法，不进行其他的操作

#   2.查看,(增删改查)类中某个，某些属性，某个方法，用万能的点.
# print(Person.animal)
# print(Person.language)

# 增
# Person.name = 'alex'
# print(Person.name)
# print(Person.__dict__)

# 改
# Person.animal = '低级动物'
# print(Person.__dict__)

# 删
# del Person.walk_way
# print(Person.__dict__)


#   3.操作方法，一般不通过类名操作
# 不建议通过__dict__执行方法
# Person.__dict__['work'](111)
# Person.work()
# 类名对静态变量（属性）进行增删改查

# 对象

class Person:
    # 静态属性（共有的）
    animal='高级动物'
    walk_way='直立行走'
    language='语言'

    # 特殊方法
    # 功能，给对象封装属性的
    def __init__(self,name,age,eye):
        self.name = name
        self.age = age
        self.eye = eye

    # 方法(相关的)
    def eat(self):
        print('该吃吃，该喝喝，啥事别忘心里搁')

    def work(self):
        print('人类都需要工作...')

# 这个过程是一个实例化的过程，他会实例化一个对象（他会在内存实例化一个对象空间）。
# obj = Person('alex',13,'小眼睛')
# print(obj)
# print(obj.name)
# 实例化过程内部进行了三个阶段
# 1.在内存中开辟了一个对象空间
# 2.自动执行类中的__init__方法，并且将对象空间传给了self参数，其他参数手动传入
# 3.执行__init__方法 给对象空间封装相应的属性


obj = Person('alex',100,'小眼睛')
# 对象
#   1.对象操作对象空间
#         对象查看对象空间所有属性 __dict__
# print(obj.__dict__)
#         对象操作对象的某个属性，（增删改查） 万能的点

# 增
# obj.sex = '男'
# print(obj.__dict__)

# 删
# del obj.eye
# print(obj.__dict__)

# 改
# obj.eye = '大眼睛'
# print(obj.__dict__)

# 查
# print(obj.name)


#   2.对象操作类空间的属性  只能查
# print(obj.animal)
# obj.animal = '低级动物'
# print(obj.animal)
# print(obj.__dict__)
#   3.对象操作类空间的方法

obj.eat()
