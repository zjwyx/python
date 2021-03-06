import socket
import os
import json
import struct
# 发送

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

# 文件名/文件大小
abs_path = r'F:\python\day30\tmp'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic)

b_dic = sk.send(str_dic.encode('utf-8'))
mlen = struct.pack('i',len(b_dic))
# 4个字节 表示字典转成字节之后的长度
sk.send(mlen)
# 具体的字典数据
sk.send(b_dic)

with open(abs_path,mode='rb') as f:
    while filesize > 0:
        content = f.read(1024)
        filesize -= len(content)
        sk.send(content)

sk.close()
