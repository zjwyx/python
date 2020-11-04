
# 1.完成以下功能
#   1.1创建一个人类Person，再类中创建3个静态变量（静态字段）
# animal= '高级动物'
# soul = '有灵魂'
# language = '语言'
#   1.2 在类中定义三个方法，吃饭，睡觉，工作
#   1.3 在此类中的__init__方法中，给对象封装五个属性：国家，姓名，性别，年龄，身高
#   1.4实例化四个人类对象：
#       第一人类对象叫p1属性为：中国，alex，未知，42,175
#       第二人类对象叫p2属性为：美国，武大，男，35,160
#       第三人类对象叫p3属性为：你自己定义
#       第四人类对象叫p4属性为：p1的国籍，p2的名字，p3的性别，p2的年龄，p3的升高
#   1.5通过p1对象执行吃饭的方法，方法里面打印：alex在吃饭
#   1.6通过p2对象执行吃饭的方法，方法里面打印：武大在吃饭
#   1.7通过p3对象执行吃饭的方法，方法里面打印：（p3对象自己的名字）在吃饭
#   1.8通过p1对象找到Person的静态变量 animal
#   1.9通过p2对象找到Person的静态变量 soul
#   2.0通过p3对象找到Person的静态变量 lange

# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self,country,name,sex,age,height):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.height = height
#
#
#     def eat(self):
#         print(f'{self.name}正在吃饭')
#
#     def sleep(self):
#         print('正在睡觉')
#
#     def hob(self):
#         print('正在工作')
#
# p1 = Person('中国','alex','未知',45,175)
# p2 = Person('美国','武大','男',35,160)
# p3 = Person('日本','西门','男',20,180)
# p4 = Person(p1.country,p2.name,p3.sex,p2.age,p3.height)

# p1.eat()
# p2.eat()
# p3.eat()


# 2.通过自己创建类，实例化对象
# 在终端输入以下信息
# 小明，10岁，男，上山砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健

# class Daylife:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def chop_wood(self):
#         print(f'{self.name},{self.age},{self.sex},上山砍柴')
#
#     def drive(self):
#         print(f'{self.name},{self.age},{self.sex},开车去东北')
#
#     def health_care(self):
#         print(f'{self.name},{self.age},{self.sex},最爱大保健')
#
# xiaoming = Daylife('小明',10,'男')
# xiaoming.chop_wood()
# xiaoming.drive()
# xiaoming.health_care()
# laoli = Daylife('老李',90,'男')
# laoli.chop_wood()
# laoli.drive()
# laoli.health_care()

# 3.模拟英雄联盟写一个游戏人物的类
# 要求：
#   1.创建一个Game_role的类
#   2.构造方法中给对象封装name.ad(攻击力)，hp（血量），三个属性
#   3.创建一个attach方法，此方法是实例化两个对象，互相攻击的功能
#       例：实例化一个对象，盖伦，ad为10，hp为100
#       例：实例化一个对象，剑豪，ad为20，hp为80
#       盖伦通过attach方法攻击剑豪，此方法要完成‘谁攻击是，谁掉了多少血，还剩多少血’的提示功能