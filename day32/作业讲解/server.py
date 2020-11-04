import socket
import json
import struct
import os
import hashlib
import sys

def get_md5(username,passowrd):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(passowrd.encode('utf-8'))
    return md5.hexdigest()

def my_send(conn,dic):
    str_dic = json.dumps(dic)
    b_dic = str_dic.encode('utf-8')
    mlen = struct.pack('i', len(b_dic))
    # 4个字节 表示字典转成字节之后的长度
    conn.send(mlen)
    # 具体的字典数据
    conn.send(b_dic)

def download():
    abs_path = r'F:\python\day30\tmp'
    filename = os.path.basename(abs_path)
    filesize = os.path.getsize(abs_path)
    dic = {'filename': filename, 'filesize': filesize}
    my_send(conn,dic)

    with open(abs_path, mode='rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            conn.send(content)

    conn.close()


def my_recv(conn):
    mag_len = conn.recv(4)
    dic_len = struct.unpack('i', mag_len)[0]
    mag = conn.recv(dic_len).decode('utf-8')
    mag = json.loads(mag)
    return mag

# 接受
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()

# 有了一个客户端未连接你
flag = True
while 1:
    # 登录
    mag = my_recv(conn)
    print(mag)
    with open('userinfo') as f:
        for line in f:
            name,pwd = line.strip().split('|')
            if name == mag['username'] and pwd == get_md5(name,mag['password']):
                res = True
                flag = False
                break
        else:
            res = False
        dic = {'operate': 'login', 'result': res}
        my_send(conn,dic)
# download()


opt_dic = my_recv(conn)
if hasattr(sys.module[__name__],opt_dic['operate']):
    getattr(sys.module[__name__],opt_dic['operate'])()
# 接受消息，根据用户的选择进行上传/下载
