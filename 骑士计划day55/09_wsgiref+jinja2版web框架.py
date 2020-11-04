'''
web框架
    返回动态的网页内容
'''

import socket
import time
from wsgiref.simple_server import make_server
import pymysql
from jinja2 import Template

# 定义处理用户请求的函数
def index(url):
    s = '你访问的是：{},这是我们的index页面'.format(url)
    with open('index.html',mode='r',encoding='utf8') as f2:
        html_S = f2.read()
    now = str(time.time())
    b = html_S.replace('@@xx@@',now)
    return bytes(b,encoding='utf8')

def home(url):
    s = '你访问的是主页面'
    return bytes(s, encoding='utf8')

def login(url):
    with open('login.html',mode='rb') as f1:
        return f1.read()

def userinfo(url):
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        port=3306,
        password="123456",
        database='day43',
        charset='utf8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from userinfo')
    user_list = cursor.fetchall()
    print(user_list)

    with open('userinfo.html','r',encoding='utf8') as f3:
        data = f3.read()

    template = Template(data)
    c = template.render(user_list)
    return [bytes(c,encoding='utf8')]


# 定义一个用户访问的url和我将要执行的函数的对应关系
url_func = [
    ('/index/',index),
    ('/home/',home),
    ('/login/',login),
    ('/userinfo/',userinfo)
]


def run_server(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset-utf8'),])
    url = environ['PATH_INFO']

    func = None
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    if func:
        msg = func(url)
    else:
        msg = b'404 Not Found'
    return [msg,]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1',8088,run_server)
    print('我在8000端口等你')
    httpd.serve_forever()
