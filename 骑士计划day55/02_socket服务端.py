import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

while 1:
    conn,addr = sk.accept()
    data = conn.recv(9000)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\nxyh dsb')
    conn.close()















