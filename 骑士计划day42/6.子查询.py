# 子查询
# 1.带in关键字的子查询
# 查询平均年龄在25岁以上的部门名
    # 首先查询平均年龄在25岁以上的部门id
    # select dep_id from employee group by dep_id having avg(age) > 25;
    # 部门id是201,202的不门信息
    # select * from department where id in (201,202);
    # 拼sql
    # select * from department where id in (
    #     select dep_id from employee group by dep_id having avg(age) > 25
    # );

# 查看技术部员工姓名
# 2.select name from employee where dep_id = (select id from department where name = '技术');
# 查看不足一人的部门名
# 3.select * from department where id not in (select dep_id from employee group by dep_id);


# 2.带比较运算符的子查询
# select avg(age) from employee;
# select name,age from employee where age > (select avg(age) from employee);






# 1、查询男生、女生的人数；
#
# 2、查询姓“张”的学生名单；
#
# 3、课程平均分从高到低显示
#
# 4、查询有课程成绩小于60分的同学的学号、姓名；
#
# 5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
#
# 6、查询出只选修了一门课程的全部学生的学号和姓名；
#
# 7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
#
# 8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
#
# 9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
#
# 10、查询平均成绩大于60分的同学的学号和平均成绩;
#
# 11、查询所有同学的学号、姓名、选课数、总成绩；
#
# 12、查询姓“李”的老师的个数；
#
# 13、查询没学过“张磊老师”课的同学的学号、姓名；
#
# 14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
#
# 15、查询学过“李平老师”所教的所有课的同学的学号、姓名；