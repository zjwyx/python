# >net start mysql 启动server端 -可以在server服务中操作
# >mysql 表示启动mysql 客户端

# mysql > select user(); 查看当前登录的用户

# mysql > show databases; 查看所有的库
# 默认的用户登录 是没有权限查看所有的库

# mysql > exit

# 指定用户登录 root用户 mysql当中的权限是最高的 管路员用户
# 用户名root

# mysql > -uroot -p
# 初始化没有密码的时候 直接按回车键进入数据库

# 在输入sql语句的过程中 如果想要放弃本条语句 \c

# 设置密码
    # mysql > set password = password('123')

