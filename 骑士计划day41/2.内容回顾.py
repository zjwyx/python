# 数据库
# 记录 表 库 数据库管理系统 数据库服务器
# 关系型数据库和非关系型数据库

# 安装和启动
# 不同的操作系统情况不同

# linux操作系统 支持长时间不关机

# sql语句
# 用户权限
# root用户 管理员账号
# 创建用户
# create user 'username'@'192.168.0.123'
# create user 'username'@'192.168.0.%'
# create user 'username'@'%'
# 通配符 _ %
# % 可以匹配任何内容

# 授权
# grant 权限
# 给已经创建的用户授权
# grant select on 库，表 to 'username'@'ip'
# grant all
# grant usage
# 创建用户并授权
# grant select on 库，表 to 'username'@'ip' identifiend by password '密码'



# 库操作
# 增加一个库  ****
# create database 名字;
# 查看库   *****
# show databases;
# 修改库
# alter database 名字 charset utf-8
# 删除库
# drop database 名字
# 使用库    *****
# use 库名;



# 表操作
# 查看当前这个库中的表
# show tables 查看当前这个库中的表
# show 库 tables 查看指定库中的表

# 创建表
# create table 表名 (列名1 数据类型 [约束]
#                   列名2 数据类型 [约束]
# )

# 查看表结构
# > desc 表名
# > describe 表名

# 删除表
# drop table 表名





# 操作记录
# 插入数据
# insert into 表名 (指定你要插入数据的字段名和顺序id,name) value(1,'alex')

# 查询数据
# select * from 表名
# select id,name from 表名


# 删除数据
# 修改数据