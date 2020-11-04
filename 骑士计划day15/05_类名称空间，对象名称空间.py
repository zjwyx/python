# 公共的模板，公共的框架
class GameRole:
    # 静态属性（共有的）
    rule = '游戏规则'

    # 方法
    # 功能，对象封装的属性
    def __init__(self,area,nickname,hp,ad):
        self.area = area
        self.nickname = nickname
        self.hp = hp
        self.ad = ad

    def attack(self):
        print('谁施展了一个攻击')

    def pen(self):
        self.pen = 10000
# 实例化对象
gailun = GameRole('德玛西亚','草丛伦',1000,75)
yasuo = GameRole('艾欧尼亚','托儿所',500,150)
penzi = GameRole('中国','键盘侠',10,100)
# penzi.pen = 10000
penzi.pen()
print(penzi.__dict__)
# 1.对象为什么能调用类中的属性和方法而且只是调用，不能修改？
# gailun.属性名  先从自己的空间去找，没有此属性他会通过类对象指针从类去找，类中找不到，会从父类去找

# print(gailun.hp)

# 给对象增加一个属性  attack = 666
# gailun.attack = 666
# print(gailun.attack)

# 游戏规则
# gailun.rule = gailun.rule
# 对象.属性名 = '游戏规则'
# print(gailun.rule)
# gailun.nickname = '盖伦'
# print(gailun.nickname)
# 对象只能查看类中的属性，不能增删改类中的属性



# 2.类能不能调用对象的属性？不能
# print(GameRole.area)


# 3.对象与对象之间可不可以互相调用？
# 同一个类实例化出来的对象之间是不能互相访问的
# 不同类实例化的对象有可能互相访问。



# 给对象封装属性：__init__任意位置，
