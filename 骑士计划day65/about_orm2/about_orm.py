import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm2.settings")

    import django
    django.setup()

    # 一对一
    # from app01.models import Author,AuthorInfo
    # obj = Author.objects.first()
    # print(obj.info.city)

    # 多对多查询
    # from app02.models import Author,Book
    # ret = Author.objects.first()
    # print(ret.books.all())

    from app03.models import Author2Book,Author,Book
    author_obj = Author.objects.filter()
    # print(author_obj.books.all())
    print(author_obj[0].books.all())

    ret = Author2Book.objects.first()
    print(ret.book)


    # Author2Book.objects.create(author_id=1,book_id=4,score=100)

