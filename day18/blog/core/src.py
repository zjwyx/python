'''
主逻辑的login，register dariy
'''

from conf import settings
from lib import common

def register():
    pass


def new_list():
    dic={}
    with open(settings.register_path,encoding='utf-8') as f1:
        for line in f1:
            line_list = line.strip().split('|')
            dic[line_list[0]] = line_list[1]
    return dic

# print(new_list())

# 登录函数
def login():
    count = 0
    dic_line = new_list()
    while count < 3:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        if username in dic_line and password == dic_line[username]:
            print('登录成功')
            status_dic['username'] = username
            status_dic['status'] = True
            return True
        else:
            print('登录失败')
        count += 1


status_dic = {
    'username':None,
    'status':False
}




@common.auth
def article():
    print('欢迎访问文章页面')

@common.auth
def comment():
    print('欢迎访问评论页面')

@common.auth
def dariy():
    print('欢迎访问日记页面')

@common.auth
def collections():
    print('欢迎访问收藏页面')

def login_out():
    pass

def quit():
    pass

dic = {
    1:login,
    2:register,
    3:article,
    4:comment,
    5:dariy,
    6:collections,
    7:login_out,
    8:quit
}

def run():
    while 1:
        print('''
            1，请先登录
            2.请注册
            3.进入文章页面
            4.进入评论页面
            5.进入日记页面
            6.进入收藏页面
            7.注销账号
            8.退出整个程序
            ''')

        num = input('请输入选项:').strip()
        num = int(num)
        dic[num]()

# run()