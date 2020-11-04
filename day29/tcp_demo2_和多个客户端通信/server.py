import socket

sk = socket.socket()
# 申请操作系统的资源
sk.bind(('127.0.0.1',9000))
sk.listen()

# 为了和多个客户端进行握手
while 1:
    # 能够和多个客户端进行握手了
    conn,addr = sk.accept()
    while 1:
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':
            break
        mag = conn.recv(1024).decode('utf-8')
        print(mag)
    # 挥手，断开连接
    conn.close()

# 归还申请的操作系统
sk.close()

# str 通过一个encode -> bytes
