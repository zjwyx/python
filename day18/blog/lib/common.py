'''
公共组件：装饰器，日志函数
'''

from core import src

def auth(f):
    '''
    你的装饰器完成，访问被装饰函数之前，写一个三次的登录认证的功能
    登录成功，让其访问被装饰的函数，登录没有成功，不让访问
    :param f:
    :return:
    '''
    def inner(*args,**kwargs):
        '''访问函数之前做的操作，功能'''
        if src.status_dic['status']:
            ret = f(*args,**kwargs)
            '''访问函数之后的操作，功能'''
            return ret
        else:
            if src.login():
                ret = f(*args,**kwargs)
                return ret
    return inner