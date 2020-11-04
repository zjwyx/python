import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))

while 1:
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'),addr)












































# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1',9000))
#
# mag,addr = sk.recvfrom(1024)
# print(mag)
# sk.sendto(b'rev',addr)
