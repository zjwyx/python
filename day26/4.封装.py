# 封装：就是把属性或者方法装起来

# 广义：把属性或者方法装起来，外面不能直接调用了,要通过类的名字来调用
# 狭义：把属性或者方法藏起来，外面不能调用，只能在内部偷偷调

# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         # 私有的实例变量，私有的对象属性
#         self.__pwd = passwd
#
# alex = User('alex','sbsbsb')
# print(alex.__pwd)    # 报错







# 给一个名字前面加上了双下划线的时候，这个名字就变成了一个私有的
# 所有的私有内容或者名字都不能在类的外部调用，只能在类的内部使用






# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         # 私有的实例变量，私有的对象属性
#         self.__pwd = passwd
#     # 表示的是用户不能改只能看，私有 + 某个get方法实现的
#     def get_pwd(self):
#         return self.__pwd
#     # 表示用户必须调用我们自定义的修改方式来进行变量的修改 私用 + change方法实现
#     def change_pwd(self):
#         pass
# alex = User('alex','sbsbsb')
# print(alex.__pwd)    # 报错








# class User:
#     # 私有的静态变量
#     __Country = '中国'
#     # 在类的内部可以调用
#     def func(self):
#         print(User.__Country)
# # 报错
# # print(User.Country)
# # print(User.__Country)
#
# User().func()





# import hashlib
# class User:
#     def __init__(self,name,passwd):
#         self.usr = name
#         # 私有的实例变量
#         self.__pwd = passwd
#     # 私有的绑定方法
#     def __get_md5(self):
#         md5 = hashlib.md5(self.usr.encode('utf-8'))
#         md5.update(self.__pwd.encode('utf-8'))
#         return md5.hexdigest()
#     def getpwd(self):
#         return self.__get_md5()
#
# alex = User('alex','sbsbsb')
# print(alex.getpwd())




# 所有的私有化都是为了让用户不在外部调用类中的某个名字
# 如果完成私有化 那么这个类的封装度就更高了 封装度越高各种属性和方法的安全性也越高，但是代码越复杂

# 加了双下划线的名字为啥不能从类的外部调用了？
# class User:
#     # 私有的静态变量
#     __Country = 'China'
#     __Role = '法师'
#     # 在类的内部使用的时候，自动把的当前这句话所在的类的名字拼在私有变量前完成变形
#     def func(self):
#         print(self.__Country)
# print(User._User__Country)
# __Country ==> '_User__Country'

# 在类的外部根本不能定义私有的概念




# 私有的内容能不能被子类使用呢？ 不能

# class Foo(object):
#     def __init__(self):
#         self.__func()
#
#     def __func(self):
#         print('in Foo')
#
#
# class Son(Foo):
#     def __func(self):
#         print('in son')
#
# Son()


# class Foo(object):
#     def __func(self):
#         print('in Foo')
#
#
# class Son(Foo):
#     def __init__(self):
#         self.__func()
#
# Son()




# 在其他语言中的数据的级别都有哪些？在python中有哪些了？

# public   公有的   类内类外都能用 父类子类都能用        python支持
# protect  保护的   类内能用 父类子类都能用，类外不能用   python不支持
# private  私有的   本类的类内部能用   去他地方都不能用   python支持

