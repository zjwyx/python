import time
import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

time.sleep(0.1)
msg1 = sk.recv(1024)
print(msg1)
msg2 = sk.recv(1024)
print(msg2)

sk.close()