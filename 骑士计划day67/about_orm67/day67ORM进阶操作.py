import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm67.settings")

    import django
    django.setup()

    from django.db.models import Avg, Max, Min, Count, Sum
    from app01.models import Book,Publisher

    # 聚合
    # 1.查询所有书的价格
    # ret = Book.objects.all().aggregate(avg_price = Avg('pric'))
    # print(ret)

    # 2.分组
    # 2.求每个出版社的名称和出版的书的数量
    # ret= Book.objects.values('publisher__pname').annotate(c=Count('id')).values_list('publisher__pname','c')
    # print(ret)

    # ret2 = Publisher.objects.values('pname').annotate(c=Count('book__id')).values_list('pname','c')
    # print(ret2)

    # 求每个出版社的名称和卖出去数书的总数
    # ret = Publisher.objects.values('pname').annotate(c=Sum('book__sale_num')).values_list('pname','c')
    # print(ret)

    # F 和 Q 查询
    from django.db.models import F,Q
    # 1.F查询
    # 查出卖出数大于收藏数的书籍
    # ret = Book.objects.filter(sale_num__gt=F('fav_num'))
    # print(ret)

    # 把所有书的价格都加1
    # Book.objects.all().update(pric = F('pric')+1)

    # Q查询
    # 找到所有价格小于10块钱或者收藏数大于10
    ret = Book.objects.filter(Q(pric__lt=10)|Q(fav_num__gt=10),sale_num__gt=100)
    print(ret)

    # 事务操作
    # from django.db import transaction
    # with transaction.atomic():
    #     # ORM语句

    # 执行原生sql
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('select * from app01_book;')
    ret = cursor.fetchall()