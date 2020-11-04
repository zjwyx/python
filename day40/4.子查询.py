# 查询姘居年龄在25岁以上的部门名

# select name from department where id in (
#     select dep_id from employee group by dep_id having avg(age) > 25
# )

# 查看技术部员工姓名
# select id from department where name='技术';

# select name from employee where dep_id in(select id from department where name='技术');
# select name from employee where dep_id=(select id from department where name='技术');



# 查看不足1人的部门（子查询得到是人的部门id）

# select disinct dep_id from employee;
# select * from department where id not in (200,202)


# 查询大于所有人平均年龄的员工与年龄
# 求平均年龄
# select avg(age) from employee;
# select name,age from employee where age > 28


# 查询大于部门内平均年龄的员工年龄，工作
# select dep_id,avg(age) from employee group by dep_id
# select name,age from employee as t1 inner join (select dep_id,avg(age) avg_avg from employee group by dep_id
# ) as t2 on t1.dep_id = t2.dep_id where age > avg_avg;


