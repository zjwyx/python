from django.shortcuts import render,redirect,HttpResponse
from app01.models import Publisher

# Create your views here.


def publisher(request):
    publisher_list = Publisher.objects.filter()
    print(publisher_list[0].name)
    return render(request,'publisher.html',{'publi':publisher_list})