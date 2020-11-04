import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       charset='utf8',
                       password="123456",
                       database='homework')

# 设置游标,可以看到sql语句走到哪了，相当于光标
cur = conn.cursor()
# 查询返回字典
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute('select * from student')
print(cur.rowcount)
# for i in range(cur.rowcount):
#     ret = cur.fetchone()  # 获取一条结果
#     print(ret)

# try:
#
#         cur.execute('select * from student')
#
#         ret = cur.fetchone()  # 获取一条结果
#         print(ret)
#
#
#         ret2 = cur.fetchmany(10)      # 获取多条结果
#         print(ret2)
#
#         ret3 = cur.fetchall() # 获取全部结果
#         print(ret3)
# except pymysql.err.ProgrammingError as e:
#         print(e)

# cur.close()
# conn.close()



# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="123456",
#                        database='homework',
#                        charset='utf8')
#
# # 设置游标
# cur = conn.cursor()
#
# # 异常处理
# try:
#         cur.execute('select * from student')
#
#         ret = cur.fetchone()
#         print(ret)
#
#         ret2 = cur.fetchmany(10)
#         print(ret2)
#
#         ret3 = cur.fetchall()
#         print(ret3)
#
# except pymysql.err.ProgrammingError as e:
#         print(e)




# import pymysql
#
# # 增加，删除，修改
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="123456",
#                        database='homework',
#                        charset='utf8')
#
# # 设置游标
# cur = conn.cursor()
# try:
#     # cur.execute('insert into student value(18,"男",3,"大壮")')
#     # cur.execute('update student set gender="女" where sid=17')
#     cur.execute('delete from student where sid=17')
#
#     conn.commit();
# except Exception as e:
#     print(e)
#     # 可以试一下myisam
#     conn.rollback()
#
# cur.close()
# conn.close()





# 实际操作mysql的时候会遇到的一个问题

# 结合数据库和pymysql写一个登录
import pymysql

user = input('username:')
pwd = input('password:')

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password="123456",
                       database='day42',
                       charset='utf8')

sql = 'select * from userinfo where user=%s and password=%s'

# 设置游标
cur = conn.cursor()
cur.execute(sql,(user,pwd))
print(cur.fetchone())


# sql注入
# select * from userinfo where user="alex" or 1=1;-- and password="3714";