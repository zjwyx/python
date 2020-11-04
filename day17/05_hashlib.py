# md5
# s1= 'dshaflkjdakljfei'
import hashlib
# ret = hashlib.md5()
# ret.update(s1.encode('utf-8'))
#
# print(ret.hexdigest(),type(ret.hexdigest()))

# import hashlib
# def MD5(pwd):
#     ret = hashlib.md5()
#     ret.update(pwd.encode('utf-8'))
#     return ret.hexdigest()
#
# def register():
#     username = input('请输入用户名：').strip()
#     password = input('请输入密码：').strip()
#     password_md5 = MD5(password)
#     with open('register',encoding='utf-8',mode='a') as f1:
#         f1.write(f'\n{password_md5}|{username}')
#
# register()
#
# def login():
#     username = input('请输入用户名：').strip()
#     password = input('请输入密码：').strip()
#     password_md5 = MD5(password)
#     with open('register',encoding='utf-8') as f1:
#         for i in f1:
#             if i[0] == password_md5:
#                 print('登录成功')
#             else:
#                 print('登录失败')




# 普通加密

# s1= 'dshaflkjdakljfei老男孩教育'
# import hashlib
# ret = hashlib.md5()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest(),type(ret.hexdigest()))


# 加盐

# s1= '19890425'
# import hashlib
# ret = hashlib.md5('太白金星'.encode('utf-8'))
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest(),type(ret.hexdigest()))


# 动态的盐
# s1= '19890425'
# import hashlib
# ret = hashlib.md5('太白金星'[::2].encode('utf-8'))
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest(),type(ret.hexdigest()))


# sha系列 金融类，安全类，用这个级别
# 随着sha系列数据越高，加密越复杂，越不容易破解，但是耗时越长
# s1= 'dshaflkjdakljfei老男孩教育'
# import hashlib
# ret = hashlib.sha3_256()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest(),type(ret.hexdigest()))





# 文件的校验

# linux中一切皆文件，文本文件，非文本文件，音频，视频，照片...
# 无论你下载的视频，还是软件（国外的软件），往往都会有一个md5值


# s1 = '我叫太白金星，今年18岁'
# import hashlib
# ret = hashlib.sha256()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest())
#
#
# ret = hashlib.sha256()
# ret.update('我叫'.encode('utf-8'))
# ret.update('太白金星，'.encode('utf-8'))
# ret.update('今年'.encode('utf-8'))
# ret.update('18岁'.encode('utf-8'))
# print(ret.hexdigest())



# low版校验：
def file_md5(path):
    ret = hashlib.sha256()
    with open(path,mode='rb') as f1:
        b1 = f1.read()
        print(b1)
        ret.update(b1)
    return ret.hexdigest()
file_md5()


# 高大上版













