import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1',9000)

while 1:
    msg = input('>>>')
    if msg.upper() == 'Q':
        break
    sk.sendto(msg.encode('utf-8'),server)
    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':
        break
    print(msg)
























# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
#
# server = ('127.0.0.1',9000)
# sk.sendto(b'hell',server)
# mag = sk.recv(1024)
# print(mag)
