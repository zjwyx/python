
# 周末作业：实现员工信息表
# 文件格式如下：
# id，name，age，phone，job
# 1，alex，22,13651504608，it
# 2，egon，23,13304320533，Teacher
# 3，nezha，25,13332355322，it



# 我们需要把数据存储在文件中，为了这个数据可以永久的保存
# 就规范了一些简单的指令，能够要求代码来完成我们的指令，从而更方便的为用户提供数据的增删改查操作
# 什么是数据库？？
# 为什么要用这么复杂的语法来操作数据库呢？
# 广义的数据库的定义，用简单的命令 就可以操作 文件中的数据




# 现在需要对这个员工信息文件进行增删改查
# 增  add boss_jin,40,13838385438,driver
# 删  del 2  模仿数据库操作
# 改  set age=18 where name='nazha'
# 查  select 必做   select name,age where age>20

# 程序开始
# input('...')  输入一个语句


# 不容许一次性将文件找那个的行都读如内存
# 基础必要
# a，可以进行查询，支持三种语法
# select 列名1，列名2，...,where 列名条件
# 支持：大于小于等于，还要支持模糊查找
# 示例：
# select name,age where age>20
# selext * where job=it
# selext * where phone like 133


