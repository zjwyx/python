'''
web框架
    根据不同的url返回不同的内容函数版
    1.先拿到用户访问的url是什么
    2.返回不同的url
'''

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8088))
sk.listen()

# 定义处理用户请求的函数
def index(url):
    s = '你访问的是：{},这是我们的index页面'.format(url)
    return bytes(s,encoding='utf8')

def home(url):
    s = '你访问的是主页面'
    return bytes(s, encoding='utf8')

while 1:
    conn,addr = sk.accept()
    data = conn.recv(9000)
    # 用户发送的请求消息
    print(data)
    # 从请求的消息中拿到请求的url是什么？
    data_str = str(data,encoding='utf8')
    # 按照\r\n分割字符串
    list = data_str.split('\r\n')
    url = list[0].split(' ')[1]
    print(url)
    if url == '/index/':
        msg = index(url)
    elif url == '/home/':
        msg = home(url)
    else:
        msg = b'404 Not Found'
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n')
    # 发送响应数据
    conn.send(msg)
    conn.close()


