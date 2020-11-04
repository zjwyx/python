class Payment:
    '''
    只要你见到了项目中有这种类，你要知道你的子类中必须实现和pay同名的方法
    '''
    def pay(self,money):
        # print('请在子类中重写同名pay方法')
        raise NotImplementedError('请在子类中重写同名pay方法')


class Alipay(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'uname':self.name,'price':money}
        # 想办法调用支付宝支付 url连接 把dic传过去
        print('%s通过支付宝支付%s钱成功'%(self.name,money))


class WeChat(Payment):
    def __init__(self,name):
        self.name = name

    def pay(self,money):
        dic = {'username':self.name,'money': money}
        # 想办法调用微信支付 url连接 把dic传过去
        print('%s通过微信支付%s钱成功' %(self.name,money))

class Apple(Payment):
    def __init__(self,name):
        self.name = name

    def pay(self,money):
        dic = {'name':self.name,'number': money}
        # 想办法调用微信支付 url连接 把dic传过去
        print('%s通过苹果支付%s钱成功' %(self.name,money))


# aw = WeChat('alex')
# aw.pay(400)
#
# aa = Alipay('alex')
# aa.pay(500)


import sys
# 归一化设计
def pay(name,price,kind):
    class_name = getattr(sys.modules['__main__'],kind)
    obj = class_name(name)
    obj.pay(price)
    # if kind == 'WeChat':
    #     obj = WeChat(name)
    # elif kind == 'Alipay':
    #     obj = Alipay(name)
    # elif kind == 'Apple':
    #     obj = Apple(name)
    # obj.pay(price)

pay('alex',400,'WeChat')
pay('alex',400,'Alipay')
pay('alex',400,'Apple')
