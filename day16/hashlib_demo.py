'''
md5加密算法

给一个数据加密的三大步骤
1.获取一个加密对象
2.使用加密对象的update进行加密，update方法可以调用多次
3.通过hexdigest获取加密结果,或者是digest方法
'''

import hashlib
# 获取一个加密对象
# m = hashlib.md5()
# # 使用加密对象的update进行加密
# m.update('abx中文'.encode('utf-8'))
# 通过hexdigest获取加密结果
# res = m.hexdigest()
# # res = m.digest()
# print(res)


# 给一个数据加密，
# 验证 用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同，如果不相同，说明与原文不同


# 不同加密算法，实际上就是加密结果的长度不同
# s = hashlib.sha224()
# s.update(b'abc')
# print(len(s.hexdigest()))
#
# print(len(hashlib.md5().hexdigest()))
# print(len(hashlib.sha256().hexdigest()))



# 在创建加密对象时，可以指定参数，称为salt
# m = hashlib.md5(b'abc')
# print(m.hexdigest())


# 注册登录功能

def get_md5(username,password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def register(username,password):
    # 加密
    res = get_md5(username,password)
    # 写入文件
    with open('login.txt',mode='at',encoding='utf-8') as f1:
        f1.write(res)
        f1.write('\n')


def login(username,password):
    # 获取当前登录信息的加密结果
    res = get_md5(username, password)
    # 读文件，和其中的数据进行对比
    with open('login.txt',encoding='utf-8',mode='rt') as f2:
        for i in f2:
            if res == i.strip():
                return True
            else:
                return False

while 1:
    op = int(input('1.注册 2.登录 3.退出:'))
    if op == 3:
        break
    elif op == 1:
        username = input('输入用户名:')
        password = input('请输入密码:')
        register(username,password)
    elif op == 2:
        username = input('输入用户名:')
        password = input('请输入密码:')
        res= login(username,password)
        if res:
            print('登录成功')
        else:
            print('登录失败')
