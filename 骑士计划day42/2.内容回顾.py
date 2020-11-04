# 数据库
# 存储引擎
    # InnoDB\MyISAM\memory\blackhole
    # InnoDB 行级锁\支持事务\外键 保持事务的完整性 在修改数据的效率高
    # MyISAM 表级锁 查询速度快 但是对插入和修改数据效率差
    # memory 数据存在内存里 处理数据的速度快 但是堆对内存要求高 且重启服务数据消失
    # blackhole 不存数据 有一个日志记录着插入的数据，利用日志分流数据

# 数据类型
    # 数值
        # tinyint smallint mediumint int bigint
        # int   2**8-1
    # 字符串
        # char      ：定长存储 查询速度快
        # varchar   ：不定长存储 查询相对慢
    # 时间
        # time date datetime year timestamp
        # date / datetime
        # timestamp / datetime
            # 范围不同：timestamp范围小，默认不能为空，时间默认是当前的时间
    # 枚举和集合
        # set('抽烟','喝酒','烫头')  去重+多选
        # enum('famle','male')  单选

# 约束
    # not null  default
    # unique auto_increment
        # unique (字段1,字段2,..)
    # primary key
        # primary key(字段1,字段2,..)
    # foreign key   本表中的字段
        # references 外表名（外表的unique字段）
        # on delete cascade
        # on update cascade

# 表的增删改查
    # drop table 表名
    # create table 表名 (
    #   列名  数据类型[长度 其他约束条件]
    #   列名  数据类型[长度 其他约束条件]
    #   列名  数据类型[长度 其他约束条件]
    # )

    # alter table 表名
                    # rename    新表名
                    # add       新列名 数据类型[长度 其他约束条件]
                    # drop      列名
                    # modify    列名  数据类型[长度 其他约束条件]
                    # change    列名 新列名  (新)数据类型[(新)长度 (新)其他约束条件]

    # 查
    # desc 表名
    # show tables;
