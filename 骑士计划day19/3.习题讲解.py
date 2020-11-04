
# 1.简述编写类和执行类中方法的流程
# 给类起个名字 class 类名 类名需要大写
# 定义静态属性，定义方法

# 实例化一个对象
# 对象名.方法名()
    # 对象在自己的内存空间中找不到方法的名字，所以就（依靠类的指针）到类中去寻找

# class Student():
#     def __init__(self):
#         self.name = 'alex'
#
#     def name(self):
#         print(12213)
#
# alex = Student()
# print(alex.name)



# 2.简述面向对象的三大特性
# 继承：提高代码的重用性，规范性
# 封装
# 多态


# 3.将以下函数改成类的方式并调用
# def func(a1):
#     print(a1)

# class A:
#     def func(self,a):
#         print(a)


# 4.方法和函数的区别
# 只有被对象调用的类中的方法才能被成为一个方法
# class A:
#     def func(self):
#         pass
#
# a = A()
# print(a.func)
# print(A.func)
#
# from types import MethodType,FunctionType
# print(isinstance(a.func,MethodType))



# 5.什么是构造函数
# 构造函数__new__



# 6.面向对象中的self值的是什么？
# self指的是对象本身

# 7.每个对象的属性存储在自己的内存空间中
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# obj = Person('孙福来',18,'女')
# 8.对象的方法，存储在类的命名空间中
# class Message:
#     def email(self): pass
#     def mag(self): pass
#     def wechat(self): pass


# 9.看代码写结果
# class Foo:
#     def func(self):
#         print('foo func')
#
# obj = Foo()
# result = obj.func()
# print(result)


# 13
# class Base1:
#     def f1(self):
#         print('base.1')
#
#     def f2(self):
#         print('base.f2')
#
#     def f3(self):
#         print('base.f3')
#         self.f1()
#
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
#
# # 多继承
# # 广度优先
# class Foo(Base1,Base2):
#     def f0(self):
#         print('f00.fo')
#         self.f3()
#
# obj = Foo()
# obj.f0()
# f00.fo
# base.f3
# base.1

# 14,报错
# class Base:
#     def f1(self):
#         print('base.f1')
#
#     def f3(self):
#         print('base.f3')
#
# class Foo(Base):
#     def f1(self):
#         print('foo.f1')
#
#     def f2(self):
#         print('foo.f2')
#
# obj2 = Base()
# obj2.f2()


# 15题

# class Person:
#     def __init__(self,name,pwd,email):
#         self.name = name
#         self.pwd = pwd
#         self.email = email
#
#
# user_list = []
# i = 0
# while True:
#     if i >= 3:break
#     i += 1
#     user = input('请输入用户名')
#     pwd = input('请输入密码')
#     email = input('请输入邮箱')
#     obj = Person(user,pwd,email)
#     user_list.append(obj)
#
# print(user_list)
# for i in user_list:
#     print(f'我是{i.name}，我的邮箱{i.email}')



# 16
class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = []

    def login(self):
        '''
        用户登录，用户输入用户名和密码并去，self_list中检查用户名合法
        :return:
        '''
        username = input('username:')
        password = input('password:')
        for i in self.user_list:
            if i.name == username and i.pwd == password:
                print('登录成功')
                return True

    def register(self):
        '''
        用户注册，动态创建User对象，并添加到self_list中
        :return:
        '''
        username = input('username:')
        password = input('password:')
        use = User(username,password)
        self.user_list.append(use)

    def run(self):
        '''
        主程序，先进行2次用户注册，在进行用户登录（3次尝试机会）
        :return:
        '''
        for i in range(2):
            self.register()

        for i in range(3):
            if self.login():
                break
        else:
            print('登录失败')

if __name__ == '__main__':
    obj = Account()
    obj.run()
