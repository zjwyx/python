import socket

sk = socket.socket()   # 买手机
sk.bind(('127.0.0.1',9000))  # 给新买的手机换上一张卡
sk.listen()  # 开机

# 等电话
conn,addr = sk.accept()
print(conn,addr)
conn.send(b'hell')
msg = conn.recv(1024)
print(msg)

conn.close()
sk.close()
