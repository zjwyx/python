
# 游戏
# 梅西，奥巴马，史努比，史派克，小猪佩奇，猪八戒   实例
# 人 狗 猪  分类
# 动物  汇总

# 先抽象 后继承




# 猫类
    # 属性：名字，品种，事物
    # 方法：叫声，抓老鼠，吃，喝，睡
# 狗类
    # 属性：名字，品种，事物
    # 方法：叫，看门，吃，喝

# class Animal:
#     def __init__(self,name,kind,food,lange):
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.lange = lange
#
#     def yell(self):
#         print(f'{self.lange}叫')
#
#     def eat(self):
#         print(f'吃{self.food}')
#
#     def drink(self):
#         print('喝水')
#
#
#
# class Cat(Animal):
#     def catch_mouse(self):
#         print('朱老鼠')
#
#
# class Dog(Animal):
#     def look_after_house(self):
#         print('看门')
#
#
# # 继承
# # 父类/超类/基类：Animal
# # 子类/派生类：Cat、Dog
#
#
# # 继承与重用
# # 父类中所有的属性和方法都可以被子类使用了
# amao = Cat('阿猫','肥猫','羊杂','喵喵')
# print(amao.name)
#
# amao.drink()
# amao.eat()
# amao.yell()



# 派生

# class Animal:
#     def __init__(self,name,kind,food,lange):
#         print('in Animal')
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.lange = lange
#
#     def yell(self):
#         print(f'{self.lange}叫')
#
#     def eat(self):
#         print(f'吃{self.food}')
#
#     def drink(self):
#         print('喝水')
#
#
#
# # Animal的派生类
# class Cat(Animal):
#     def __init__(self,name,kind,food,lange,eye_color):
#         print('in Cat')
#         # super().__init__(name,kind,food,lange)
#         Animal.__init__(self,name,kind,food,lange)
#
#         # 派生属性
#         self.eye_color = eye_color
#     # 派生方法
#     def catch_mouse(self):
#         print('抓老鼠')
#
#     # 不仅执行了父类找那个的基础功能，还完成了特殊的功能
#     def eat(self):
#         # Animal.eat(self)
#         super().eat()
#         self.weight = 10
#
#
# class Dog(Animal):
#     def look_after_house(self):
#         print('看家')
#
#     def eat(self):
#         Animal.eat(self)
#         self.drink()
#
# amao = Cat('阿猫','橘猫','羊杂','喵喵','绿色')
# print(amao.eye_color)
# print(amao.food)
# amao.catch_mouse()
# amao.eat()
# print(amao.weight)

# 当子类当中有要被调用的方法的时候，子类的对象会直接选择子类中的方法，变量
# 父类中的方法不会被自动执行
# 如果我们既想要执行子类的方法，也想要执行父类的方法，那么需要在子类的方法中调用父类的方法
# 父类.方法名(self...)
# super().方法名(...)
# 帮助我们在子类中调用父类的同名方法


# 面试题
# 当self去调用某个方法的时候，不要看self在哪个类里面，要看self到底是谁
# class Foo:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print('in Foo')
#
#
# class Son(Foo):
#     def func(self):
#         print('in Son')
#
# s1 = Son()



# class Foo:
#     County = 'China'
#     def func(self):
#         print(self.County)
#
# class Son:
#     County = 'Englise'
#     # 走这个方法
#     def func(self):
#         print(self.County)
#
#
# s = Son()
# s.func()



# class Foo:
#     County = 'China'
#     def func(self):
#         print(self.County)
#
# class Son(Foo):
#     County = 'Englise'
#
#
#
# s = Son()
# # Englise
# s.func()


# class Foo:
#     County = 'China'
#
#     def func(self):
#         print(self.County)
#
#
# class Son(Foo): pass
#
#
# s = Son()
# # Englise
# s.func()
