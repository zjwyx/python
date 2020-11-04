# 所谓连表
    # 总是在连接的时候创建一张大表，里面存放的是两张表的笛卡尔积
    # 再根据条件进行筛选就可以了



# 表与表之间的连接方式
    # select * from 表1,表2 where 条件;
    # 内连接 inner join ... on ...
        # select * from 表1 inner join 表2 on 条件
        # select * from department inner join employee on departyment.id = employee.dep_id;
        # select * from department as t1 inner join employee as t2 on t1.id = t2.dep_id;
# 外连接
    # 左外连接  left join ... on ...
        # select * from 表1 left join 表2 on 条件
        # select * from department as t1 left join employee as t2 on t1.id = t2.dep_id;

    # 右外连接  right join ... on ...
        # select * from 表1 right join 表2 on 条件
        # select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;

    # 全外连接 full join
        # select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;
        # unio
        # select * from department as t1 left join employee as t2 on t1.id = t2.dep_id;


# 题
# 1.找到技术部的人的所有姓名
# select t2.name from department as t1 inner join employee as t2 on t1.id = t2.dep_id where t1.
# name='技术';

# 2.找到人力资源部的年龄大于40岁的姓名
# select t2.name from department as t1 inner join employee as t2 on t1.id = t2.dep_id where t1.
# name='人力资源' and t1.age > 40;


# 所谓连表就是把两张表连接在一起之后，变成一张大表，从from开始一直到on条件结束就看做一张大表
# 之后where条件 group by分组 order by排序 limit都可以正常的使用就可以了
