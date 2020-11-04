# 多表查询
    # 连表查
        # 内连接 必须左表和右表中条件互相匹配的项才会被显示出来
            # 表1 inner join 表2 on 条件
    # 外连接
        # left join     左表显示全部，右表中的数据必须和左表条件匹配的项才会被像是出来
        # right join    右表显示全部，左表中的数据必须和右表条件匹配的项才会被像是出来
        # 全外连接
            # left join
            # union
            # right join
    # 子查询
        # select * from 表 where 字段 in (select 字段 from 表 where 条件)
        # select * from 表 where 字段 = (select 字段 from 表 where 条件)
        # select * from 表 where 字段 > (select 字段 from 表 where 条件)



# 5 题
# select * from score where student_id=1;
#
# select course_id from score where student_id=1;
# select * from score where course_id in (1,2,4);
#
# select distinct student_id from score where course_id in (
#     select course_id from score where student_id=1
# ) and student_id != 1;
#
# select sid,name from student right join (
# select distinct student_id from score where course_id in (
#     select course_id from score where student_id=1
# ) and student_id != 1) as t on student.sid = t.student.id


# select distinct student_id,sname from student as t1 inner join score as t2 on t1.sid = t2.student_id where course_id in (select * from score where student_id=1);
# select * from score where student_id=1;

# 8 题
# 把课程编号为2的所有人的学生id，成绩找出来
# select student_id as sid2,num as n2 from score where course_id = 2;

# 把课程编号为1的所有人的学生id，成绩找出来
# select student_id as sid1,num as n1 from score where course_id = 1;

# 课程编号2的成绩比课程编号1课程低的所有同学的学号
'''
select sid1 from (select student_id as sid2,num as n2 from score where course_id = 2) as t2
    inner join
    (select student_id as sid1,num as n1 from score where course_id = 1) as t1
    on t1.sid1 = t2.sid2 where n2 < n1;
'''
# select sid,sname from student right join (
# select sid1 from (select student_id as sid2,num as n2 from score where course_id = 2) as t2
#     inner join
#     (select student_id as sid1,num as n1 from score where course_id = 1) as t1
#     on t1.sid1 = t2.sid2 where n2 < n1
# ) as tmp
# on student.sid = tmp.sid1;




# 9 题
# 先获取生物课的id
# select cid from course where cname='生物';
# 先获取物理课的id
# select cid from course where cname='物理';
# 找到所有学物理的人
# select student_id as sid2,num as n2 from score where course_id = (select cid from course where cname='生物');
# select student_id as sid2,num as n2 from score where course_id = (select cid from course where cname='物理');

# select sid1 from (select student_id as sid1,num as n2 from score where course_id = (select cid from course where cname='生物')) t1
# inner join
# (select student_id as sid2,num as n2 from score where course_id = (select cid from course where cname='物理')) as t2
# on t1.sid1 = t2.sid2 where n2 > n1;


# 13 题
# 找一下张磊老师教什么课，课程id
# select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '张磊';
# 在从score表中找到学习张磊老师课程的学生
# select distinct student_id from score where course_id in (select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '张磊')
# 再找不是这些学生的其他人
# select sid,sname from student where sid not in (
#     select distinct student_id from score where course_id in (select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '张磊')
# );


# 15 题
# 找到李平老师教的课程
# select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师';
# 找到所有学习李平老师的学生
# select * from score where course_id in (
#     select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师'
# );
#
# 查询学号
# select student_id,count(*) from score where course_id in (
#     select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师'
# ) group by student_id having count(*) = (
#     select count(id) from course inner join teacher on course,teacher_id = teacher.tid where tname = '李平老师'
# );

# 查询姓名
# select * from student right join (
#     select student_id,count(*) from score where course_id in (
#         select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师'
#     ) group by student_id having count(*) = (
#         select count(id) from course inner join teacher on course,teacher_id = teacher.tid where tname = '李平老师'
#     )
# ) as tmp on tmp.student_id = student.sid;
