'''
获取用户输入，登录
'''

import pymysql
pymysql.connect



# 1.获取用户输入
name = input('请输入用户名：')
pwd = input('请输入密码：')

# 判断用户名和密码是否正确
# 去数据库查询一下 用户输入的用户名和密码是否正确

# 1.连接数据库,得到一个连接
conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    database = 'day43',
    charset = 'utf8'
)

# 2.获取光标
cursor = conn.cursor()
# 3.执行sql语句
# 3.1 得到SQL语句
# 按照pymysql模块的写法定义好占位符
sql = "select * from userinfo where username = %s and password = %s;"
print(sql)
# 3.2使用光标对象执行sql语句
# 让pymysql模块帮我们拼接mysql语句，执行sql语句
ret = cursor.execute(sql,[name,pwd])

# 关闭
cursor.close()
conn.close()

# 4.得到结果
if ret:
    print('登录成功')
else:
    print('登录失败')
