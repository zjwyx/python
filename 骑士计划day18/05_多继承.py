
# class Parent1:pass
# class Parent2:pass
# class Son(Parent1,Parent2):pass
#
# print(Son.__bases__)


# 不是所有的语言都支持多继承，java
# c++ 支持多继承


# 天鹅  飞，游泳，走路
# 老虎   走路，游泳
# 鹦鹉   飞，说话，走路
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def talk(self):
#         print(f'{self.name}说话了')
#
#     def fly(self):
#         print(f'{self.name}在飞')
#
#     def walk(self):
#         print(f'{self.name}在走路')
#
#     def swim(self):
#         print(f'{self.name}在游泳')

class Animal:
    def __init__(self,name):
        self.name = name

class FlyAnimal(Animal):
    def fly(self):
        print(f'{self.name}在飞')

class WalkAnimal(Animal):
    def walk(self):
        print(f'{self.name}在走路')

class SwimAnimal(Animal):
    def swim(self):
        print(f'{self.name}在游泳')



class Tiger(SwimAnimal,WalkAnimal):
    pass


class Swan(FlyAnimal,SwimAnimal,WalkAnimal):
    pass


class Parrot(FlyAnimal,WalkAnimal):
    pass
    def talk(self):
        print(f'{self.name}说话了')


swan = Swan('天鹅')
swan.fly()
