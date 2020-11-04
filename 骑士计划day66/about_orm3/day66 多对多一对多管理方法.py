import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm67.settings")

    import django
    django.setup()

    from app01.models import MyClass,Student,Teacher

    # 1.查询id=1的班级的所有学生
    # ret = MyClass.objects.get(id=2).student_set.all()
    # print(ret)
    # # 2.查询id = 2的班级的所有老师
    # ret2 = MyClass.objects.get(id=2).teacher_set.all()
    # print(ret2)

    # 给id=1的班级添加一个id=5的学生
    # ret3 = MyClass.objects.get(id=1).student_set.all()
    # print(ret3)
    # 先找到id=5的学生
    # student = Student.objects.get(id=5)
    # MyClass.objects.get(id=1).student_set.add(student)
    # ret3 = MyClass.objects.get(id=1).student_set.all()
    # print(ret3)

    # 把所有的学生都绑定给id=1的班级中
    student = Student.objects.all()
    ret4 = MyClass.objects.get(id=1).student_set.set(student)
    print(ret4)

    Teacher.objects.get(id=2).myclass.create(cname='生理课')
    # add create remove clear set
    # 一对多种remove 和 clear 使用规则
    # 必须外键关联的ForeignKey中有null=True属性
