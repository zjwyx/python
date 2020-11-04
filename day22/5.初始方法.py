class Person:
    # 必须叫这个名字，不能改变，所有的在一个具体的人物出现之后拥有的属性
    def __init__(self,name,sex,job,level,hp,weapon,ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.ad = ad

    def eat(self,dog):
        dog.blood -= self.ad
        print(f'{self.name}给{dog.name}搓澡，{dog.name}掉了{self.ad}点血，{dog.name}剩下{dog.blood}血量')

class Dog():
    def __init__(self,name,blood,aggr,kind):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.kind = kind

    def slep(self,people):
        people.hp -= self.aggr
        print(f'{self.name}攻击了{people.name},{people.name}掉了{self.aggr},人的血量剩余{people.hp}')

小白 = Dog('小白',5000,249,'柯基')

alex = Person('alex','不详','搓澡工',0,250,'搓澡工',1)

alex.eat(小白)

小白.slep(alex)
