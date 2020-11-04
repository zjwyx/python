import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm67.settings")

    import django
    django.setup()

    from app01.models import Teacher,Student,MyClass

    # alex老师带过的班级的学生
    ret = Teacher.objects.filter(tname='alex').values('myclass__student__sname')
    print(ret)