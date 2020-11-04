from gevent import monkey
monkey.patch_all()
import socket
import gevent

def func(conn):
    while 1:
        msg = conn.recv(1024).decode('utf-8')
        MSG = msg.upper()
        conn.send(MSG.encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()

while 1:
    conn,addr = sk.accept()
    gevent.spawn(func,conn)
