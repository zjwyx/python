# 插入数据  insert into
# 更新数据  update set
# 删除数据  delete
# 查询数据  select * from




# 单表查询
# 从表中查询条件
# select (distinct) 字段1,字段2,... from 表名
#                       where 条件
#                       group by field    根据某个字段分组
#                       having 筛选        根据分组的结果进行筛选
#
#                       order by field     根据查询结果排序
#                       limit 限制条数      从结果中查找n条



# 查询名字和工资
# select emp_name,salary from employee;
# # 避免重复 distinct
# select distinct post from employee;
# # 查看总工资  四则运算
# select emp_name,salary*12 from employee;
# # 重命名
# select emp_name,salary*12 ysalary from employee;
# # 拼接
# select concat('员工':emp_name,'年薪':salary*12) from employee;
# select concat_ws(':'emp_name,salary*12,age,sex) from employee;
#
# select (
#     case
#     when emp_name = 'jinliyang'
#     then emp_name
#     when emp_name = 'alex'
#     then concat(emp_name,'_bigsb')
#     else
#     concat(emp_name,'sb')
#     end
# ) as new_name
# from employee;


# 练习
# 1.select concat('<名字':emp_name'>,<薪资':salary '>') from emplayee;
# 2.select distinct post from employee;
# 3.select emp_name,salay *12 as annual_year from employee;











# where 过滤约束   （行）
# 1.比较运算符：< > >= <= <> !=
# 2.between 80 and 100 值在80到100之间
# 3.in(80,90,100) 值是80或90或100
# 4.like 'egon%'
#     %表示任意多个字符
#     _表示一个字符
# select emp_name from employee where salary > 2000
# select emp_name from employee where between 5000 and 8000
# select emp_name from employee where post in ('teacher','sale')
# select emp_name from employee where emp_name like 'j%';
# select emp_name from employee where emp_name like '程_';


# 练习
# 1.select emp_name,age from employee where post = 'teacher';
# 2.select emp_name,age from employee where post = 'teacher' and age > 30;
# 3.select emp_name,age,salay from employee where pose = 'teacher' and salay between 9000 and 10000;
# 4.select * from employee where post_comment not null;  != null;
# 5.select emp_name,age,salay from employee where post = 'teacher' and salay in (10000,30000,90000);
# 6.select emp_name,age,salay from employee where post = 'teacher' and salay not in (10000,30000,90000);
# 7.select emp_name,salay*12 from  employee where name like 'jin%';



# group by  分组
# select * from employee group by post;
# select post,group_concat(emp_name) from employee group by post;

# 聚合函数
# select post,count(id) from employee where group by post;
# count
# avg
# min
# max
# group_concat
# 分组和聚合使用

# 练习
# 1.select post,group_concat(emp_name) from employee group by post
# 2.select post,count(emp_name) from employee group by post;
# 3.select sex,count(id) from employee group by sex;
# 4.select post,avg(salay) from employee group by post;
# 5.select post,max(salay) from employee group by post;
# 6.select post,min(salay) from employee group by salay;
# 7.select sex,avg(salay) from employee groub by sex;



# having 过滤     （对组进行过滤  group by 和 having  是搭档）
# 1.select post,count(id),group_concat(emp_name) from employee group by having count(id) < 2;
# 3.select post,avg(salay) from employee group by post having avg(salay) > 10000;
# 4.select post,avg(salay) from employee group by post having avg(salay) between 10000 and 20000;




# order by  排序
# select * from employee order by salary;
# 从大到小
# select * from employee order by salary desc;
# select * from employee order by age,hire_date desc;

# 练习
# select post,avg(salay) from employee group by post having avg(salay) > 1000 order by avg(salay);


# limit 限制查询的记录数

# 使用正则表达式查询
# select * from employee where emp_name regexp '^ale';

