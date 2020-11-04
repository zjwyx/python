'''
向userinfo表查询所有数据
'''

import pymysql

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
sql = "select * from userinfo;"

# 3.2使用光标对象执行sql语句
# 让pymysql模块帮我们拼接mysql语句，执行sql语句
cursor.execute(sql)
ret = cursor.fetchall()
print(ret)
# 关闭
cursor.close()
conn.close()


