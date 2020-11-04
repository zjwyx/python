import socket
friend_lst = {'alex':'32','太白':'33'}


sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))

while 1:
    msg,addr = sk.recvfrom(1024)
    msg = msg.decode('utf-8')
    name,message = msg.split('|')

    print('\033[1;%sm %s:%s\033[0m'%(friend_lst.get(name,'30'),name,message))
    content = input('>>>').encode('utf-8')
    sk.sendto(content,addr)
    if content.upper() == 'Q':
        break
