
# 工作中，公司有使用抽象类开发的规则
# 源码 别人使用抽象类

# 支付功能

# 模板的功能
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self): pass

    @abstractmethod
    def shouqina(self): pass


class Alipay(Payment):
    def pay(self,money):
        print(f'使用支付宝支付了{money}')

class Wechatpay(Payment):
    def pay(self, money):
        print(f'使用微信支付了{money}')

class ApplePay(Payment):
    def pay(self,money):
        print(f'使用applepay支付了{money}')



def pay(obj,money):
    obj.pay(money)

a = Alipay()

pay(a,100)


# 规范
# 多人开发，复杂的需求，后期的扩展
# 手段 来帮助我们完成规范

# 抽象类
    # 抽象类是一个规范，，他基本不会实现什么具体的功能，抽象类是不能实例化的
    # 要想写一个抽象类
        # from abc import ABCMeta,abstractmethod
        # 在这个类创建的时候指定 metaclass=ABCMeta
        # 在你子类实现的方法上加上一个 @abstractmethod 装饰器
    # 使用抽象类
        # 继承这个类
        # 必须实现这个类中的被 @abstractmethod 装饰器装饰的方法
