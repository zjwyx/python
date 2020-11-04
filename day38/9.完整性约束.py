# 约束某一个字段不能为空
# 不能为空  not null
# 无符号的  int unsigned
# 默认值
# 不能重复
# 自增
# 主键
# 外键

# create table t10(
#     id int unsigned
# )


# create table t11(
#     id int unsigned not null
#     name char(18) not null
# );


# create table t12(
#     id int unsigned not null
#     name char(18) not null
#     male enum('male','female') not null default 'male'
# );


# 不能重复  unique
# create table t13(
#     id int unique
#     id2 int
# )


# 联合唯一 unique
# create table t14(
#     id int,
#     server_name char(12)
#     ip char(15)
#     port char(5)
#     unique(ip,port)
# );


# 非空 + 唯一约束
# 第一个被定义为非空 + 唯一的那一列会成为这张表的primary key
# 一张表只能定义一个主键
# create table t15(
#     id int not null unique,
#     username char(18) not null unique
# );
#
#
# create table t16(
#     id int not null unique,
#     username char(18) not null unique
# );
#
#
# create table t15(
#     id int primary key,
#     username char(18) not null unique
# );


# 联合主键
