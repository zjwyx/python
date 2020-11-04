# 定义一个圆类，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形
    # 计算圆形面积
    # 计算圆的周长


# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#
#     def mianji(self):
#         return pi*self.r*self.r
#
#     def zhouchang(self):
#         return 2*pi*self.f
#
# file = Circle(5)
# print(file.mianji())
# print(file.zhouchang())
#
# tel = Circle(10)
# print(tel.mianji())




# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
    # 登录成功之后才能创建用户对象
    # 设计一个方法 修改方法

import os

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def change_pwd(self):
        oldpwd = input('输入原密码:')
        newpwd = input('输入新密码:')
        with open('userinfo', encoding='utf-8') as f1, open('userinfo.bak', encoding='utf-8', mode='w') as f2:
            for line in f1:
                username, password = line.strip().split('|')
                if username == self.username and password == oldpwd:
                    line = '%s|%s\n' % (username, newpwd)
                f2.write(line)

        os.remove('userinfo')
        os.rename('userinfo.bak', 'userinfo')


# xiaoming = User('小明',123456)
# xiaohong = User('小红',123456789)

name = input('username:')
passwd = input('password:')

def login(name,passwd,filepath = 'userinfo'):
    with open(filepath,encoding='utf-8') as f:
        for line in f:
            user,pwd = line.strip().split('|')
            if user == name and pwd == passwd:
                return True
            else:
                return False
ret = login(name,passwd)

if ret:
    print('登录成功')
    obj = User(name,passwd)
    obj.change_pwd()
