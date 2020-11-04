from django.shortcuts import render,HttpResponse,redirect
from app01.models import UserInfo
from django import views
from django.urls import reverse

# Create your views here.


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         pwd = request.POST.get('pwd')
#         ret = UserInfo.objects.filter(username=username,pwd=pwd)
#         if ret:
#             return HttpResponse('登录成功')
#
#     return render(request,'login.html')


# CBV
class LofinVies(views.View):
    def get(self,request):
        print(request.path_info)
        print(request.get_full_path())
        return render(request,'login.html')

    def post(self,request):
        print('='*120)
        print(request.body)
        print(request.POST)
        print(request.META)
        if request.method == 'POST':
            username = request.POST.get('username')
            pwd = request.POST.get('pwd')
            ret = UserInfo.objects.filter(username=username, pwd=pwd)
            if ret:
                print(reverse('index_list'))
                return redirect(reverse('app02:index_list'))
            else:
                return render(request,'login.html')


# 上传文件实例
class UploadView(views.View):

    def get(self,request):
        return render(request,'upload.html')

    def post(self,request):
        print(request.POST)
        # 获取文件类型的数据
        print(request.FILES)
        print(request.FILES.get('filename'))
        print(request.FILES.get('filename'),type(request.FILES.get('filename')))
        # 你上传，我写入
        filename_obj = request.FILES.get('filename')
        filename = filename_obj.name
        # 在当前的项目目录下新建一个和上传文件文件名相同的文件
        with open(filename,'wb') as f:
            for i in filename_obj:
                f.write(i)

        return HttpResponse('收到了')



def json_data(request):
    d = {
        'name':'阿玟',
        'age':24,
        'school':'清华'
    }
    import json
    # str = json.dumps(d,ensure_ascii=False)
    # return HttpResponse(str,content_type='application/json')
    from django.http import JsonResponse
    return JsonResponse(d)


# 路由系统
def book(request,year):
    # 匹配出来的类型是字符串
    print(year,type(year))
    return HttpResponse('Book')


def book_list(request):
    return HttpResponse('书籍列表页面')

def blog(request,num=1):
    print(num)
    return HttpResponse('博客页面')



# 上传文件练习
def upload2(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.FILES.get('file'),type(request.FILES.get('file')))
        file_obj = request.FILES.get('file')
        file = file_obj.name
        with open(file,'wb') as f:
            for i in file_obj:
                f.write(i)
        return HttpResponse('收到了')
    return render(request,'upload2.html')