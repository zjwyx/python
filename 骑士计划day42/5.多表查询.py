# 直接查询
# 表与表之间产生了一个暴力全集 --- 笛卡尔积
# [a,b,c],[1,2,3]
# a1,b1,c1,a1,b2,c2,a3,b3,c3
#
#
# 内连接   inner join
# select * from 表1 inner join 表2 on 表1.外键字段 = 表2.字段
# 只有两个表中互相匹配的项才能被显示在新表中
#
# employee id name sex age dep_id
# department id name
#
# select * from employee t1 inner join department t2 on t1.dep_id = t2.id;
# 筛选
# select t1.id,t1.name,t2.name from employee t1 inner join department t2 on t1.dep_id = t2.id;
#
# 左连接
# select * from employee t1 left join department t2 on t1.dep_id = t2.id
#
# 右链接
# select * from employee t1 right join department t2 on t1.dep_id = t2.id


# 全外连接
# select * from employee t1 left join department t2 on t1.dep_id = t2.id
# union
# select * from employee t1 right join department t2 on t1.dep_id = t2.id




# 练习
# select t1.name as emp_name,t2.name as dep_name from employee t1 inner join department t2 on t1.dep_id = t2.id where t1.age>25;
# select t1.name as emp_name,t2.name as dep_name from employee t1 inner join department t2 on t1.dep_id = t2.id order by t1.age;
