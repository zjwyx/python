"""mysiteday63 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
from app02 import url as app02_url

urlpatterns = [
    # url(r'^login/', views.login),
    url(r'^login/$', views.LofinVies.as_view()),
    url(r'^upload/$', views.UploadView.as_view()),
    url(r'^json_data/$', views.json_data),
    url(r'^upload2/',views.upload2),
    # 路由系统
    url(r'^book/$',views.book_list),
    url(r'^book/([0-9]{4})/$',views.book),  # book(request,2018)
    url(r'^book/([0-9]{4})/([0-9]{2})/$',views.book),  # book(request,2018)
    # url(r'^book/(?P<yyyy>[0-9]{4})/$',views.book),  # book(request,yyyy=2018)
    url(r'^blog/$',views.blog),
    url(r'^blog/(?P<num>\d+)/$',views.blog),

    # 二级路由
    # namespace='app02' 在HTML和视图页面中指定
    url(r'^app02/',include(app02_url,namespace='app02'))
]
