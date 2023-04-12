import os
import subprocess
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render, HttpResponse, redirect

from app01.models import UserInfo,Photo

# Create your views here.
def index(request):
    return render(request, "index.html")


def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/index/")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("user")
        password = request.POST.get("password")
        #数据库校验用户名和密码
        # admin_object = models.
        admin_object = UserInfo.objects.filter(name=username,password=password).first()

        if not admin_object:
            return_dic = {
                'str': "用户名或密码错误",
            }
            return render(request, "login.html",return_dic)

        #用户名和密码正确
        #网站生成随机字符串，写到用户浏览器的cookie中，再写入到session中
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.name}
        return redirect("/index/")

def register(request):
    if request.method == "GET":
        return render(request, "register.html",)
    else:
        username = request.POST.get("user")
        password = request.POST.get("password")
        # photo = request.FILES.get("photo")
        # print(request)
        UserInfo.objects.create(name=username,password=password)
        # Photo.objects.create(username=username,priPhotoDate=photo)
        # user = Photo.objects.filter(id=11)
        return redirect("/login/")



#------------------------testPic----------------
def userPage(request):
    #获取到session用户的所有图片进行展示
    if request.method == "GET":
        info = request.session.get("info")
        photo_object = Photo.objects.filter(username=info["name"])
        return render(request, "userPage.html",{"photo_object":photo_object})
    else:
        username = request.POST.get("user")
        password = request.POST.get("password")
        pic  = request.POST.get("photo")
        # photo = request.FILES.get("photo")
        print(request)
        print(username)
        print(password)
        print(pic)
        #UserInfo.objects.create(name=username,password=password)
        # Photo.objects.create(username=username,priPhotoDate=photo)
        # user = Photo.objects.filter(id=11)
        return render(request, "userPage.html")

def uploadPic(request):
    # 检查用户是否已登陆，已登录继续向下走，未登录跳转登陆页面
    # 用户发来请求，获取cookie随机字符串，拿着随机字符串看看session中有没有
    # 用户登录过就获取字典，没登陆过就获取一个none
    # info = request.session.get("info")
    # print(info)
    # if not info:
    #     return redirect('/login/')

    if request.method == "GET":
        return render(request, "uploadPic.html")
    else:
        img = request.FILES.get("img")
        img_name = img.name
        mobile = os.path.splitext(img_name)[0]
        ext = os.path.splitext(img_name)[1]
        img_name = f'avatar-{mobile}{ext}'

        # 图片保存路径
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)

        # 写入 上传图片的 内容
        with open(img_path, 'ab') as fp:
            # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
            for chunk in img.chunks():
                fp.write(chunk)
        print(img_path)
        # Photo.objects.create(username=username,priPhotoDate=photo)
        # user = Photo.objects.filter(id=11)
        p = subprocess.Popen('python D:\CODE\python\yolov5-7.0\detect.py '+"--source " + img_path, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        out = p.stdout.readlines()
        print(out)
        path = "../static/uploads"+"/"+img_name
        path2 = "../static/media"+"/"+img_name
        info = request.session.get("info")
        Photo.objects.create(username=info["name"], priPhotoDate=path2,photoDate=path)

        return_dic = {
            'str': path,
            'str2':path2,
        }

        return render(request, "uploadPic.html",return_dic)


def picDelete(request):
    pid = request.GET.get('pid')
    Photo.objects.filter(id=pid).delete()
    return redirect("/userPage/")
