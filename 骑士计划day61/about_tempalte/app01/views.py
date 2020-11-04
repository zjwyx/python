from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime,timedelta
# Create your views here.

def t(request):
    d1 = {'name':'夏宇航','age':15}

    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age =  age

        @staticmethod
        def dream():
            return 'write the code,change the word'

    wxts = Person('元成名',30)

    p1 = Person('小明',20)
    p2 = Person('小红',30)
    p3 = Person('小钢',40)

    list1 = ['游鸿亮','网上','夏宇航','李清扬','元成名']
    list2 = [p1,p2,p3]

    return render(request,'t.html',{'name':'王帅','d1':d1,'sb':wxts,'f5':list1,'f6':list2})

# filter相关的语法
def t2(request):
    name = '夏宇航'
    file_size = 1234567890
    now = datetime.now()
    a = '<a href="https://www.baidu.com">百度</a>'
    p = '在苍茫的大海上，狂风卷积这乌云，在乌云和大海之间，海燕像黑色的闪电，在高傲的飞翔'
    p_1 = '在 苍 茫 的 大 海 上 ，狂风卷积这乌云，在乌云和大海之间，海燕像黑色的闪电，在高傲的飞翔'
    p_2 = 'alexalexdsb'
    list1 = ['游鸿亮', '网上', '夏宇航', '李清扬', '元成名']

    # 获取五个小时之前的时间
    hours5 = now - timedelta(hours=5)
    # --------------day62--------------------------
    now = datetime.now()
    t1 = now - timedelta(seconds=3)
    t2 = now - timedelta(minutes=3)
    t3 = now - timedelta(minutes=30)

    return render(request,
                  't2.html',
                  {
                      'name':name,
                      'file_size':file_size,
                      'now':now,
                      'a':a,
                      'p':p,
                      'p_1':p_1,
                      'p_2':p_2,
                      'list1':list1,
                      'hourse5':hours5,
                      't1':t1,
                      't2':t2,
                      't3':t3,
                  })