# __new__

# class A:
#     # 构造方法
#     def __new__(cls, *args, **kwargs):
#         o = super().__new__(cls)
#         print('执行new',o)
#         return o
#
#
#     def __init__(self):
#         print('执行init',self)
#
# A()

# 实例化的时候
# 先创建一块对象的空间，有一个指针能指向类---> __new__
# 调用init --->  __init__




# 面试的时候用(背)
# 设计模式 -- 单例模式
# 一个类 从头到尾 只会创建一次self的空间
class Baby:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,cloth,pants):
        self.cloth = cloth
        self.panth = pants

b1 = Baby('红毛衣','绿皮裤')
b2 = Baby('白衬衫','黑袍文')

print(b1.cloth)
print(b2.cloth)
