import sys

class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd



class Accout:
    def __init__(self):
        self.user_list = []

    def login(self):
        # 登录
        # 登录 输入用户名密码
        # 和self.user_list比较
        username = input('用户名：')
        password = input('密码：')
        for user in self.user_list:
            if username == user.name and password == user.pwd:
                print('登录成功')
                break
            else:
                print('登录失败')

    def register(self):
        # 注册
        # 注册成功了，user对象存在user_list里
        username = input('用户名：')
        password = input('密码：')
        password2 = input('密码确认：')
        if password == password2:
            user = User(username,password)
            self.user_list.append(user)
            print('登录成功')
        else:
            print('注册失败，您两次密码不一致')

    def run(self):
        opt_lst = ['登录','注册']
        while 1:
            for index,item in enumerate(opt_lst,1):
                print(index,item)
            num = input('请输入您操作的序号:')
            # obj_number = getattr(sys.modules['__main__'],num)
            # obj = obj_number()
            # obj.login()
            if num == '1':
                self.login()
            elif num == '2':
                self.register()
            elif num.upper() == 'Q':
                break

if __name__ == '__main__':
    obj = Accout()
    obj.run()

# 注册之后，重启所有的用户丢失
# 一次执行的注册行为，在之后所有执行中都能够正常登录
# 两个登录程序和面向对象的内容整理在一起，两个都要明白，都要记住



# class Foo(object):
#     n1 = 'alex'
#     def __init__(self,name):
#         self.n2 = name
#
#
# obj = Foo('太白')
# print(obj.n1)
# print(obj.n2)
#
#
# print(Foo.n1)
# print(Foo.n2)  # 报错
