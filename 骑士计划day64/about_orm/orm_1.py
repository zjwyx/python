import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

    import django
    django.setup()

    from app01.models import UserInfo

    ret = UserInfo.objects.all()
    print(ret)