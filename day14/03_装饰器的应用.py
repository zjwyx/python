

def login():
    pass

def register():
    pass


status_dic = {
    'username':None,
    'status':False
}

def auth(f):
    '''
    你的装饰器完成，访问被装饰函数之前，写一个三次的登录认证的功能
    登录成功，让其访问被装饰的函数，登录没有成功，不让访问
    :param f:
    :return:
    '''
    def inner(*args,**kwargs):
        '''访问函数之前做的操作，功能'''
        if status_dic['status']:
            ret = f(*args,**kwargs)
            '''访问函数之后的操作，功能'''
            return ret
        else:
            username = input('请输入姓名：').strip()
            password = input('请输入密码：').strip()
            if username == 'alex' and password == '123':
                print('登录成功')
                status_dic['username'] = username
                status_dic['status'] = True
                ret = f(*args,**kwargs)
                return ret
            else:
                print('登录失败')
    return inner


@auth
def article():
    print('欢迎访问文章页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')

article()
comment()
dariy()