'''
向userinfo表把alex删除
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
sql = "delete from userinfo where username = %s;"

# 3.2使用光标对象执行sql语句
# 让pymysql模块帮我们拼接mysql语句，执行sql语句
ret = cursor.execute(sql,['alex'])
# 涉及到操作数据库的 一定要提交
conn.commit()
# 关闭
cursor.close()
conn.close()


