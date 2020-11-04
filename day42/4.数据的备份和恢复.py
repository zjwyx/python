# 表和数据的备份
    # 在cmd命令行直接执行
    # 备份数据
    # mysqldump -uroot -p123456 -h127.0.0.1 homework > F:\python\day42\tmp.sql

    # 恢复数据 在mysql中执行命令
    # 切换到一个要备份的数据库中
    # source F:\python\day42\tmp.sql

# 备份库
    # 备份
    # mysqldump -uroot -p123456 --databases homework > F:\python\day42\tmp2.sql
    # 恢复
    # source F:\python\day42\tmp2.sql
