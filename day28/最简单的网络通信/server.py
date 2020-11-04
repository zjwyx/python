import socket

# 创建一个server端的对象
sk = socket.socket()
# 给server端绑定一个地址
sk.bind(('127.0.0.1',9000))
# 开始监听（可以接受）客户端给我的连接
sk.listen()

# 建立连接 conn是连接
conn,addr = sk.accept()
conn.send(b'hell')
mag = conn.recv(1024)
print(mag)
# 关闭连接
conn.close()

# 关闭整个服务
sk.close()




















