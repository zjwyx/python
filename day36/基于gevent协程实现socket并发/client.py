import socket
import time
from threading import Thread

def client():
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))

    while 1:
        sk.send(b'hello')
        msg = sk.recv(1024)
        print(msg)
        time.sleep(0.5)

for i in range(500):
    Thread(target=client).start()
