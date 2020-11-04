# 先来定义模子，用来描述一类事物
# 具有相同属性和动作

# class Person:
#     # 必须叫这个名字，不能改变，所有的在一个具体的人物出现之后拥有的属性
#     def __init__(self,name,sex,job,level,hp,weapon,ad):
#         self.name = name
#         self.sex = sex
#         self.job = job
#         self.level = level
#         self.hp = hp
#         self.weapon = weapon
#         self.ad = ad
#
# # alex就是对象，alex = Person()的过程 是通过类或的一个对象的过程 - 实例化
# alex = Person('alex','不详','搓澡工',0,250,'搓澡工',1)
# # 查看所有属性
# # print(alex.__dict__)
#
# print(alex.name)
#
# # 属性的修改
# alex.name = 'sb'
# print(alex.name)
#
# # 属性的增加
# alex.money = 10000
# print(alex.money)
# print(alex.__dict__)
#
# # 属性的删除
# del alex.money
# print(alex.__dict__)

# 类名() 会自动调用类中的__init__方法

# 类和对象之间的关系？
    # 类 是一个大范围 是一个模子 它约束了事物有哪些属性 但是不能约束具体的值
    # 对象 是一个具体的内容 是楔子的产物 它遵循了类的约束 同时给属性附上具体的值


# person 是一个类 ，alex，wusir都是这个类的对象

# 类有一个空间，存储的是定义在class中的所有名字
# 每一个对象又拥有自己的空间，通过对象名.__dict__就可以查看这个对象的属性和值

# 查看所有的属性：__dict__








# d = {'k':'v'}
# d['k'] = 'vvvv'


# 修改列表\字典中的某个值，或者是对象的某一个属性 都不会影响真个对象\字典\列表所在的内存空间



# 实例化所经历的步骤：
    # 1.类名() 之后的第一个事儿：开辟一块内存空间
    # 2.调用__init__ 把空间的内存地址作为self参数传递到函数内部
    # 3.所有的这一个对象需要使用的属性都需要和self关联起来
    # 4.执行完init中的逻辑之后，self变量会自动的被返回到调用处（发生实例化的地方）


# dog类 实现狗的属性 名字 品种 血量 攻击力 都是可以被通过实例化被定制的
# class Dog():
#     def __init__(self,name,blood,aggr,kind):
#         self.name = name
#         self.blood = blood
#         self.aggr = aggr
#         self.kind = kind
#
# Dog('小白',5000,249,'柯基')


# 定义一个圆类，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形
    # 计算圆形面积
    # 计算圆的周长
# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
    # 登录成功之后才能创建用户对象
    # 设计一个方法 修改方法
# 继续完成人狗大战
    # 你是人
    # 狗是一个npc
    # 你一个回合 狗一个回合
    # 狗掉的血是一个波动值
    # 闪避值

# 继续完成计算器




class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

xiaoming = User('小明',123456)
xiaohong = User('小红',123456789)

# class Yuan:
#     def __init__(self,banjing):
#         self.banjing = banjing
#
#     def mianji(self):
#         print(3.14*self.banjing*self.banjing)
#     def zhouchang(self):
#         print(2*3.14*self.banjing)
#
# file = Yuan(5)
# tel = Yuan(10)
#
# file.mianji()
# file.zhouchang()

# tel.mianji()