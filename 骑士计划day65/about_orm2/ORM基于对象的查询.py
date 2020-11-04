import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm2.settings")

    import django
    django.setup()

    from app01.models import Book,Author,AuthorInfo,Publisher
    book_obj = Book.objects.first()
    print(book_obj.title)
    print(book_obj.publisher.name)

    publisher_obj = Publisher.objects.get(name='世外桃源出版社')
    ret = publisher_obj.book_set.all()
    print(ret)