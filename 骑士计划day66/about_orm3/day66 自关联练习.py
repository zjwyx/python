import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm67.settings")

    import django
    django.setup()

    from app02.models import Comment
    # id=2的评论的所有子评论
    ret = Comment.objects.filter(pcomment_id=2)
    print(ret)
