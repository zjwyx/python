'''
web框架
    根据不同的url返回不同的内容
    1.先拿到用户访问的url是什么
    2.返回不同的url
'''

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8088))
sk.listen()

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
        msg = 'this is index page'
    elif url == '/home/':
        msg = 'this is home page'
    else:
        msg = '404 Not Found'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # 发送响应数据
    conn.send(bytes(msg,encoding='utf8'))
    conn.close()
