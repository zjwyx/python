from django.shortcuts import render
from app01.models import UserInfo
# Create your views here.


def home(request):
    # 列表
    user_obj = UserInfo.objects.all()[0]
    print(user_obj.name,type(user_obj.name))
    print(user_obj.birthday,type(user_obj.birthday))
    print(user_obj.gender,type(user_obj.gender))
    print(user_obj.get_gender_display())
    return render(request,'home.html')