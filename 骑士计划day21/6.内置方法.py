
# 在不是需要程序员定义，本身就存在类中的方法就是内置方法
# 内置的方法通常都长这样：__名字__
# 名字：双下方法，魔术方法，内置方法


# __init__
    # 不需要主动的调用，而是在实例化的时候内部自动调用的

# 所有的双下方法，都不需要我们直接去调用，都是另外一种自动触发它的语法

# __str__  __repr__
# class Counter:
#     def __init__(self,name,period,price,teacher):
#         self.name = name
#         self.period = period
#         self.price = price
#         self.teacher = teacher
#
#     def __str__(self):
#         return 'str : %s %s %s %s' %(self.name,self.period,self.price,self.teacher)
#
#     def __repr__(self):
#         return 'repr : %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
#
# course_lst = []
# python = Counter('python','6 month',2900,'bass jin')
# course_lst.append(python)
# linux = Counter('linux','5 month',28000,'alex')
# course_lst.append(linux)
#
# for id,course in enumerate(course_lst):
#     # print(f'{id},{course.name},{course.period},{course.price},{course.teacher}')
#     print(id,course)
#     print('%s %s' %(id,course))
#     print(str(course))
#     print(repr(course))


# __str__
# 当你打印一个对象的时候触发__str__
# 当你使用 %s 格式化的时候，触发__str__
# str强转数据类型的时候，触发__str__


# __repr__
# repr是str的备胎
# 有__str__的时候执行__str__,没有实现__str__的时候，执行__repr__
# repr(obj)内置函数对象的结果__repr__的返回值
# 当你使用 %s 格式化的时候，触发__repr__


# 学生选择课程的时候，要显示所有的课程

# class Foo:
#     def __str__(self):
#         return 'Foo str'
#
#     def __repr__(self):
#         return 'Foo repr'
#
#
# class Son(Foo):
#     # def __str__(self):
#     #     return 'Soo str'
#     def __repr__(self):
#         return 'Soo repr'
#
# s1 = Son()
# print(s1)
