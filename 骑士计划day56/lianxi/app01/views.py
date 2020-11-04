from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect,HttpResponse
from app01.models import userInfo,Publisher

def login(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        ret = userInfo.objects.filter(email=email,password=pwd)

        if ret:
            return redirect('/index/')
        else:
            return render(request,'login.html',{'error_msg':'用户名或者密码错误'})

    return render(request,'login.html')

def index(request):
    return render(request,'index.html')


# 出版社列表页面的处理函数
def publisher_list(request):
    # 1.去数据库中把所有的出版社数据取出来
    ret = Publisher.objects.all()
    print(ret)
    print(ret[0],type(ret[0]))
    print(ret[0].id)
    print(ret[0].name)
    # 2.在页面上把出版社数据显示出来
    return render(request,'publisher_list.html',{'publisher_list':ret})

# 出版社的增
def addlisher_list(request):
    # 判断请求的方式是不是post
    # 表示用户填写了信息，提交过来
    # 1.获取用户填写的信息
    # 2.添加到数据库中
    # 3.给用户返回提示
    if request.method == 'POST':
        print(request.POST)
        new_name = request.POST.get('publisher_name')
        Publisher.objects.create(name=new_name)
        return redirect('/publisher_list/')

    return render(request,'addlisher_list.html')

# 删除
def deletelish_list(request):
    print(request.GET)
    delete_id = request.GET.get('id')
    Publisher.objects.filter(id=delete_id).delete()

    return redirect('/publisher_list/')

# 修改出版社
def edith_list(request):
    if request.method == 'POST':
        new_edit = request.POST.get('edit_name')
        new_id = request.POST.get('id')
        edit_obj = Publisher.objects.get(id=new_id)
        edit_obj.name = new_edit
        edit_obj.save()
        return redirect('/publisher_list/')
    # 1.获取要编辑的出版社的id
    edit_id = request.GET.get('id')
    # 2.根据id去数据库拿到要编辑的出版社数据
    ret = Publisher.objects.get(id=edit_id)
    print(ret,type(ret))
    # 3.在页面上显示 要编辑的出版社信息
    return render(request,'edit_list.html',{'obj':ret})

