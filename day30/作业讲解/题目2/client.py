import socket
name = '太白'

sk = socket.socket(type=socket.SOCK_DGRAM)

while 1:
    content = input('>>>').encode('utf-8')

    if content.upper() == 'Q':
        break
    content = '%s|%s' %(name, content)
    sk.sendto(content.encode('utf-8'),('127.0.0.1',9000))
    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':
        break
    print(msg)
