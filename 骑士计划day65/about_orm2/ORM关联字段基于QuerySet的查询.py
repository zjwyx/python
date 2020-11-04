import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm2.settings")

    import django
    django.setup()

    from app01.models import Book,Publisher

    ret = Book.objects.filter(id=1).values('publisher__addr')
    print(ret)

    ret1 = Publisher.objects.filter(id=1).values('book__title')
    print(ret1)

