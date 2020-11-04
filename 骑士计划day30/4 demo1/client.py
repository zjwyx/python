import socket

sk = socket.socket()   # 买手机
sk.connect(('127.0.0.1',9000))   # 打电话

msg = sk.recv(1024)
print(msg)
sk.send(b'bybye')

# 关闭
sk.close()
