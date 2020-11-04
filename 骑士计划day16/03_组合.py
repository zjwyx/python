# 3.模拟英雄联盟写一个游戏人物的类
# 要求：
#   1.创建一个Game_role的类
#   2.构造方法中给对象封装name.ad(攻击力)，hp（血量），三个属性
#   3.创建一个attach方法，此方法是实例化两个对象，互相攻击的功能
#       例：实例化一个对象，盖伦，ad为10，hp为100
#       例：实例化一个对象，剑豪，ad为20，hp为80
#       盖伦通过attach方法攻击剑豪，此方法要完成‘谁攻击是，谁掉了多少血，还剩多少血’的提示功能


# 组合：给一个类的对象封装一个属性，这个属性是另一个类的对象

# class Gamerole:
#
#     def __init__(self,nickname,ad,hd):
#         self.nickname = nickname
#         self.ad = ad
#         self.hd = hd
#
#     # 攻击方法
#     def attack(self,role):
#         role.hd = role.hd - self.ad
#         print(f'{self.nickname}攻击是{role.nickname}，{role.nickname}掉了{self.ad}血，还剩{role.hd}血')
#
#     # 武器方法
#     def equip_weaon(self,w):
#         self.weapon = w
#
#
#
# class Weapon:
#     def __init__(self,name,ad):
#         self.name = name
#         self.ad = ad
#
#
#     def fight(self,role,role1):
#         role1.hd = role1.hd - self.ad
#         print(f'{role.nickname}用{self.name}攻击了{role1.nickname}，{role1.nickname}掉了{self.ad}血,换剩下{role1.hd}血')
#
# p1 = Gamerole('盖伦',20,500)
# p2 = Gamerole('剑豪',100,200)
#
# # p1.attack(p2)
# # print(p2.hd)
# # 这样不好，动作的发起者应该是人而不是武器
# # w1.fight(p1,p2)
#
# w1 = Weapon('大宝剑',30)
# w2 = Weapon('武士刀',80)
# # print(w1)
# p1.equip_weaon(w1)
# # 其实就是w1
# # print(p1.weapon)
# p1.weapon.fight(p1,p2)
#
# # 剑豪利用武士刀给了盖伦一刀
# # p2.weapon.fight(p1,p2)
# p2.equip_weaon(w2)
# p2.weapon.fight(p2,p1)







































# class Gamerole:
#     def __init__(self,nickname,ad,hp):
#         self.nickname = nickname
#         self.ad = ad
#         self.hp = hp
#
#     # 攻击方法
#     def attack(self,role):
#         role.hp = role.hp - self.ad
#         print(f'{self.nickname}攻击了{role.nickname}，{role.nickname}掉了{self.ad}血，还剩下{role.hp}血')
#
#     # 武器方法
#     # 给人物封装了一个武器属性，这个属性值是Weapon类的一个对象
#     def equip_weaon(self,w):
#         self.weapon = w
#
#
# class Weapon:
#
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def fight(self,role,role1):
#         role1.hp = role1.hp - self.ad
#         print(f'{role.nickname}用{self.name}攻击了{role1.nickname}，{role1.nickname}掉了{self.ad}血,换剩下{role1.hp}血')
#
#
# p1 = Gamerole('盖伦',20,500)
# p2 = Gamerole('剑豪',100,200)
#
# # p1.attack(p2)
#
#
# w1 = Weapon('大宝剑',20)
# w2 = Weapon('武士刀',80)
#
# # 这样不好，用武器类调用英雄类
# # w1.fight(p1,p2)
#
# # 解决方法，给英雄类添加一个属性，作为武器类的对象
# # 执行equip_weaon方法，给p1添加了一个weapon属性，指向w1
# p1.equip_weaon(w1)
# print(p1.weapon)
# print(w1)
# p1.weapon.fight(p1,p2)
#
# p2.equip_weaon(w2)
# p2.weapon.fight(p2,p1)
#
# # 组合的意义：让类的对象与另一个类的对象产生关系，类与类产生关系







# 人物类
class Gamerole:
    def __init__(self,nickname,ad,hp):
        self.nickname = nickname
        self.ad = ad
        self.hp = hp

    # 攻击方法
    def attack(self,role):
        role.hp = role.hp - self.ad
        print(f'{self.nickname}攻击了{role.nickname}，{role.nickname}掉了{self.ad}血，还剩下{role.hp}血')

p1 = Gamerole('盖伦',20,500)
p2 = Gamerole('剑豪',100,200)
p1.attack(p2)


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def fight(self,role,role1):
        role1.hp = role1.hp - self.ad
        print(f'{role.nickname}用{self.name}攻击了{role1.nickname}，{role1.nickname}掉了{self.ad}血,换剩下{role1.hp}血')

w1 = Weapon('大宝剑',20)
w2 = Weapon('武士刀',80)

# 一个类的对象成为另一个类对象的属性
# 盖伦使用大宝剑攻击剑豪

p1.gongji = w1
p1.gongji.fight(p1,p2)