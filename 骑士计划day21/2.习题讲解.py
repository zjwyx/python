# 1.类变量(静态属性)和实例变量(对象属性)的区别?
# 2.super的作用?       在子类中调用父类的方法.
# 一般情况下,子类中有和父类相同的方法名
# 3.ininstance和type的区别并用代码举例说明?
# ininstance能判断对象与类之间的继承关系
# type 只能判断这个对象是哪个类创建出来的

# 4.补全代码

# def func(age):
#     if callable(age):
#         ret = age()
#         print(ret)
#     else:
#         print('else',age)
#
# class Foo: pass
#
# # 类可以被调用，而对象不行
# # func(Foo)
# obj = Foo()
# func(obj)



# 5.补全代码
# from types import MethodType,FunctionType
# def func(*args):
#     funxion_count = 0
#     method_count = 0
#     foo_obj = 0
#     for item in args:
#         if isinstance(item,FunctionType):
#             funxion_count += 1
#         elif isinstance(item,MethodType):
#             method_count += 1
#         elif isinstance(item,Foo):
#             foo_obj += 1
#     return {'function_count':funxion_count,'method_count':method_count,'foo_obj':foo_obj}
#
# def func1():
#     pass
# def func2():
#     pass
#
# class Foo:
#     def method1(self):
#         pass
#     def method2(self):
#         pass
#     def method3(self):
#         pass
#
# f1 = Foo()
# f2 = Foo()
# ret = func(func1,func2,f1.method1(),Foo.method1,Foo(),Foo())
# print(ret)


# 6题
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11,22]
#
# s1 = StarkConfig();
# s2 = StarkConfig();
#
# result1 = s1.get_list_display()
# print(result1)
#
# result2 = s2.get_list_display()
# print(result2)




# 7题
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11,22]
#
# s1 = StarkConfig();
# s2 = RoleConfig();
#
# result1 = s1.get_list_display()
# print(result1)
#
# result2 = s2.get_list_display()
# print(result2)


# 8题
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11,22]
#
# s1 = RoleConfig();
# s2 = RoleConfig();
#
# result1 = s1.get_list_display()
# print(result1)
#
# result2 = s2.get_list_display()
# print(result2)