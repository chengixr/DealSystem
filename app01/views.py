
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import requests
import time


def index(request):
    return HttpResponse("Hello World")


def user_list(request):
    # 1.优先去项目目录的templates中寻找[需配置，不配置就是无效]
    # 2.根据app的注册顺序，逐一去他们的templates目录里去找
    return render(request, "user_list.html")


def tpl(request):
    name = "承浩"
    roles = ["程序员", "boss", "经理"]
    user_info = {"name": "承浩", "age": 24, "salary": 10000}
    print("path:", request.path)
    print("method:", request.method)
    print("user:", request.user)
    user1 = models.SysUsers.objects.filter(USERID='CHENGHAO')
    print(user1)
    return render(request, "tpl.html", {"n1": name, "n2": roles, "n3": user_info})


def something(request):
    # 1.获取请求方式 GET/POST
    print(request.method)

    # 2.在URL上传递参数 something/?n1=1223&n2=23912
    print(request.GET)

    # 3.在请求体中请求数据
    print(request.POST)

    # 4.将字符串内容返回给请求者
    # return HttpResponse("返回内容")

    # 5.读取html的内容 + 渲染（替换） -> 字符串，返回给请求者
    # return render(request, "something.html")

    # 6.让浏览器重定向到指定页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    print(request.POST)
    login_id = request.POST.get("user")
    login_pwd = request.POST.get("pwd")
    if request.POST.get("register"):
        return redirect("http://127.0.0.1:8000/register/")
    user_login = models.SysUsers.objects.filter(USERID=login_id).filter(PASSWOED=login_pwd)
    print(user_login)
    if user_login:
        return redirect("https://www.baidu.com")
    elif login_id == "" and login_pwd == "":
        return render(request, "login.html")
    else:
        return render(request, "login.html", {"error_msg": "用户名或密码不正确"})


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    find_user = models.SysUsers.objects.filter(USERID=request.POST.get("userid"))
    if find_user:
        return render(request, "register.html", {"error_msg": "用户已存在"})
    print(find_user)

    print(request.POST)
    user_id = request.POST.get("userid")
    user_name = request.POST.get("username")
    org_id = request.POST.get("org_id")
    org_name = request.POST.get("org_name")
    user_class = request.POST.get("user_class")
    user_idcard = request.POST.get("user_idcard")
    admin_flag = request.POST.get("admin_flag")
    user_status = request.POST.get("user_status")
    user_sex = request.POST.get("user_sex")
    user_email = request.POST.get("user_email")
    user_phone = request.POST.get("user_phone")
    creat_user = models.SysUsers.objects.create(
        USERID=user_id, USERNAME=user_name, ORGID=org_id, PASSWOED='111111', USERCLASS=user_class, IDCARD=user_idcard,
        ADMINFLAG=admin_flag, STATUS=user_status, SEX=user_sex, EMAIL=user_email, TELNO=user_phone,
        CREATDATE=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        LSTMNDATE=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        EFFECTFLAG='E'
    )
    print(creat_user, type(creat_user))
    return render(request, "login.html")


def secinfo(request):
    if request.method == "GET":
        return render(request, 'secinfo.HTML')
