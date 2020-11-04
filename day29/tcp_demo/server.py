# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# conn.send(b'hell')
# mag = conn.recv(1024)
# print(mag)
# conn.close()
#
# sk.close()









import socket

sk = socket.socket()
# 申请操作系统的资源
sk.bind(('127.0.0.1',9000))
sk.listen()

# conn里存储的是一个客户端和server端的连接信息
conn,addr = sk.accept()
conn.send(b'hell')
mag = conn.recv(1024)
print(mag)
# 挥手，断开连接
conn.close()

# 归还申请的操作系统
sk.close()

