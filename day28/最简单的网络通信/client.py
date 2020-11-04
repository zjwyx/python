import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))


mag = sk.recv(1024)
print(mag)

sk.send(b'byebye')

sk.close()