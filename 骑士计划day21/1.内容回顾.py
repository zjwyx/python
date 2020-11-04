
# class A:
#     @property
#     # 这个方法的返回值就是（a.func）结果
#     def func(self):
#         pass
#
# a = A()
# print(a.func())
# 把一个方法伪装成一个属性


# class A:
#
#     @property
#     # 这个方法的返回值就是（a.func）结果
#     def func(self):
#         return self.name
#
#     @func.setter
#     # 修改操作
#     def func(self,new):
#         self.name = new
#
#
# a = A()
# print(a.func())
# a.func = 123



# class A:
#     @property
#     # 这个方法的返回值就是（a.func）结果
#     def func(self):
#         return self.name
#
#     @func.deleter
#     # 删除一个property属性的时候会执行被deleter装饰的方法
#     def func(self):
#         del self.name
#
# del A().func

# setter
# delete

















# classmethod
# 在类中定义一类方法
# 是一个装饰器
# 什么时候用？
    # 如果你的整个方法中都没有用到对象命名空间中的名字，且你用到了类的命名空间中的名字（普通方法和property方法除外）
# 类方法的默认参数：cls值得是调用这个方法的类
# 类方法的调用方式：通过类名调用


# 在类的命名空间中有什么？
# 静态属性
# 方法
# 类方法
# 静态方法
# property方法







# staticmethod
# 将一个普通的函数放到类中来就给这个函数加上一个@staticmethod装饰器
# 这个函数就不需要传默认的参数：self，cls
# 静态方法的调用方式：通过类名调用,本质还是函数
class Foo:
    @staticmethod
    def class_method(self): pass

    @staticmethod
    def static_method(): pass

from types import MethodType,FunctionType
obj = Foo()
print(isinstance(Foo.class_method,FunctionType))
print(isinstance(Foo.static_method,FunctionType))
print(obj.static_method)
















# isinstance
# 判断对象和类之间的关系
# 判断这个对象是否是这个类，这个类的子类的对象


# issubclass
# 判断类和类之间的关系
# 判断回一个类是否是另一类的子类
