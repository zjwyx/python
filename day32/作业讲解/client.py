import socket
import json
import struct
import sys

# 下载
def download():
    opt_dic = {'operate':'download'}
    my_send(sk,opt_dic)
    mag = my_recv(sk)

    with open(mag['filename'], 'wb') as f:
        while mag['filesize'] > 0:
            content = sk.recv(1024)
            mag['filesize'] -= len(content)
            f.write(content)


# 发送
def my_send(sk,dic):
    str_dic = json.dumps(dic)
    b_dic = str_dic.encode('utf-8')
    mlen = struct.pack('i', len(b_dic))
    # 4个字节 表示字典转成字节之后的长度
    sk.send(mlen)
    # 具体的字典数据
    sk.send(b_dic)


# 接受
def my_recv(sk):
    mag_len = sk.recv(4)
    dic_len = struct.unpack('i', mag_len)[0]
    mag = sk.recv(dic_len).decode('utf-8')
    mag = json.loads(mag)
    return mag


# 发送
sk = socket.socket()
sk.connect(('127.0.0.1',9000))


def login(sk):
    # 登录
    while 1:
        usr = input('用户名：').strip()
        pwd = input('密码：').strip()
        dic = {'username':usr,'password':pwd}
        my_send(sk,dic)
        ret = my_recv(sk)
        if ret['operate'] == 'login' and ret['result']:
            print('登录成功')
        else:
            print('登录失败')


login(sk)
# 上传和下载
opt_lst = ['upload','download']
for index,opt in enumerate(opt_lst,1):
    print(index,opt)
num = int(input('请输入您要操作的序号：'))
getattr(sys.module[__name__],opt_lst[num-1])(sk)

sk.close()

