# 存储引擎
    # Innodb  mysql5.6之后默认存储引擎
        # 2个文件，4个支持(支持事物，行级锁，表级锁，外键)
    # Myisam
        # 3个文件 支持表级锁
    # Memory
        # 1个文件 数据段断电消失
# 数据类型
    # 数字    ：int，float
    # 字符串   ：
        # char  定长，效率高浪费空间 255
        # varchar   变长 效率低节省空间  65535
    # 日期    ：date time datetime year
    # enum和set
        # 单选和多选

# 约束
    # unsigned  无符号的
    # not null  不能为空
    # default   默认值
    # unique    唯一，不能重复
    # unique(字段一，字段二)   联合唯一
    # primarry key 主键
        # not null + unique
        # 一张表只能有一个主键
    # foreign key   外键
        # a表中有一个字段关联b表中的unique
        # a表中的是外键
    # auto_increnent    自增
        # int 必须至少unique字段 自带not null
# 建表
    # create table 表名(
    #     字段名1 类型(长度) 约束
    # )
# 修改表结构
    # alter table 表名 rename
    # alter table 表名 add
    # alter table 表名 drop
    # alter table 表名 modify
    # alter table 表名 change
# 表与表之间的关系
    # 一对一
    # 一对多
    # 多对多
