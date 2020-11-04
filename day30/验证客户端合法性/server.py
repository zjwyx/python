import socket
import os
import hashlib

secret_key = b'alex_sb'
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
# 创建一个随机的字符串
rand = os.urandom(32)
conn.send(rand)

sha = hashlib.sha1(secret_key)
sha.update(rand)
res = sha.hexdigest()

res_client = conn.recv(1024).decode('utf-8')
if res_client == res:
    print('是合法的客户端')
    conn.send(b'hell')
else:
    conn.close()
# 发送随机字符串
# 根据发送的字符串 + server key进行摘要
# 等待接收客户端的摘要结果
# 做对比
# 如果一致，就显示是合法的客户端
# 并可以继续操作
# 如果不一致 应立即关闭连接
