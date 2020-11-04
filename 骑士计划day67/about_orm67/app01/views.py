from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def index(request):
    if request.method =='POST':
        num = request.POST.get('num')
        print('前端输入的内容是:',num)
        return HttpResponse(num)
    return render(request,'index.html')