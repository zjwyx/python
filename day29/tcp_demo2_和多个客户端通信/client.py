import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

while 1:
    mag = sk.recv(1024)
    mag2 = mag.decode('utf-8')
    if mag2.upper() == 'Q':
        break
    print(mag2)
    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q':
        break

sk.close()