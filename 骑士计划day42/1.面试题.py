# 1.mysql常见数据库引擎及比较
# InnoDB\MyISAM\memory\blackhole
# InnoDB 行级锁\支持事务\外键 保持事务的完整性 在修改数据的效率高
# MyISAM 表级锁 查询速度快 但是对插入和修改数据效率差
# memory 数据存在内存里 处理数据的速度快 但是堆对内存要求高 且重启服务数据消失
# blackhole 不存数据 有一个日志记录着插入的数据，利用日志分流数据


# 2.什么是事务？mysql如何支持事务
# 事务 就是将一组sql语句当做一个原子性操作
# 要么全部成功，要么全部不成功
# MySQL如何支持事务
# 指定表的存储引擎为InnoDB

# 3.简述数据库中一对多和多对多的应用场景


# 4.主键和外键的区别
# 主键：一张表只能有一个主键，主键非空且唯一
# 外键：一张表可以有多个外键，可以重复

# 5.如何判断是函数还是方法
# from types import FunctionType,MethodType
# class A:
#     def func(self):
#         pass
# a = A()
#
# # 类调用的是一个函数
# # 实例化调用的是一个方法
# print(isinstance(a.func,FunctionType))
# print(isinstance(A.func,FunctionType))
#
# print(isinstance(a.func,MethodType))
# print(isinstance(A.func,MethodType))
