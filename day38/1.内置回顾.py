
# 数据库：DB
    # 所有的数据存放的仓库
    # 每一个文件夹也是一个数据库
# 数据库管理软件  --- 软件 DBMS
    # 关系型数据库：mysql，oracle，sqllite， sql server，db2，access
    # 非关系型数据库：redis mongoose memcache
# 数据库管理员 DBA
    # 管理数据库软件
# 数据库服务器：一台跑着一个数据库管理软件的机器
# 表：文件，一张存储数据的表
# 数据/记录：表中的信息，一行就是一条记录


# 用户相关操作
# 查看当前用户是谁？ select user()
# 给当前用户设置密码 set password = password('123')
# 创建用户 create user '用户名'@'主机名的ip/主机域名' identified by '密码'
# 授权 grant select on 数据库名 * to '用户名'@'主机名的ip/主机域名'  identified by '密码'
# 创建用户 grant select on 数据库名 * to '用户名'@'主机名的ip/主机域名'


# 基础的库\表\数据操作

# 库 - 文件夹
    # 创建库---------------------- create database 数据库名;
    # 创建到这个库 ---------------- use 库名;
    # 查看所有的库 ---------------- show databases;
# 表 - 文件
    # 查看这个库下的所有表 ---- show tables;
    # 创建表 ----------------- create table 表名(字段名 数据类型（长度）,字段名 数据类型（长度）);
    # 删除表 ----------------- drop table 表名;
    # 查看表结构 ---------------- desc 表名;
        # describe 表名;
# 数据（记录） - 文件中的内容
# 增：insert into 表 value (一行数据),(一行数据),(一行数据);
# 删: delete from 表 where 条件;
# 改：update 表 set 字段名=值,字段名2=值2 where 条件;
# 查: select * from 表














































































