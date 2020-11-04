from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse('app02的博客主页面')