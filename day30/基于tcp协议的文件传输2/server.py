import socket
import json
# 接收

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
mag = conn.recv(1024).decode('utf-8')
mag = json.loads(mag)

with open(mag['filename'],'wb') as f:
    while mag['filesize'] > 0:
        content = conn.recv(1024)
        mag['filesize'] -= len(content)
        f.write(content)

conn.close()
sk.close()



























