'''
获取用户输入，登录
'''

# 1.获取用户输入
username = input('请输入用户名：')
password = input('请输入密码：')

# 判断用户名和密码是否正确
if username == 'alex' and password == 'alexsb':
    print('登录成功')
else:
    print('登录失败')
