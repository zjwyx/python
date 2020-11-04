# 用字符串数据类型的名字 来操作这个名字对应的函数\实例变量\绑定方法\各种方法


# name = 'alex'
# age = 123
#
# n = input('>>>')
# if n == 'name':
#     print(name)
# elif n == 'age':
#     print(age)




# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def qqxing(self):
#         print('qqxing')
#
# alex = Person('alex',83)
# wusir = Person('wusir',74)
#
#
# ret = getattr(alex,'name')
# print(ret)
#
# ret = getattr(wusir,'name')
# print(ret)
#
# ret = getattr(alex,'qqxing')
# ret()






# class Payment:
#     '''
#     只要你见到了项目中有这种类，你要知道你的子类中必须实现和pay同名的方法
#     '''
#     def pay(self,money):
#         # print('请在子类中重写同名pay方法')
#         raise NotImplementedError('请在子类中重写同名pay方法')
#
#
# class Alipay(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'uname':self.name,'price':money}
#         # 想办法调用支付宝支付 url连接 把dic传过去
#         print('%s通过支付宝支付%s钱成功'%(self.name,money))
#
#
# class WeChat(Payment):
#     def __init__(self,name):
#         self.name = name
#
#     def pay(self,money):
#         dic = {'username':self.name,'money': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功' %(self.name,money))
#
# class Apple(Payment):
#     def __init__(self,name):
#         self.name = name
#
#     def pay(self,money):
#         dic = {'name':self.name,'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' %(self.name,money))
#
#
# aw = WeChat('alex')
# aw.pay(400)
#
# aa = Alipay('alex')
# aa.pay(500)
#
#
# # 归一化设计
# def pay(name,price,kind):
#     if kind == 'WeChat':
#         obj = WeChat(name)
#     elif kind == 'Alipay':
#         obj = Alipay(name)
#     elif kind == 'Apple':
#         obj = Apple(name)
#     obj.pay(price)
#
# pay('alex',400,'WeChat')
# pay('alex',400,'Alipay')
# pay('alex',400,'Apple')




# import a
# print(a.Wechat)
# print(a.Alipay)
#
# # 对象名.属性名 ===> getattr(对象名,'属性名')
# # a.Alipay ===> getattr(a,'Alipay')
#
# print(getattr(a,'Alipay'))
# print(getattr(a,'Wechat'))

# 'Wechat'
# 'Alipay'


# class Wechat:pass
# class Alipay:pass

# import a
# import sys
# print(sys.modules['a'])
# print(a.Alipay)
# print(getattr(a,'Alipay'))
# print(getattr(sys.modules['a'],'Alipay'))



# wahaha = 'hahaha'
# print(getattr(sys.modules['__main__'],'wahaha'))
