from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    """中间件1"""
    def process_request(self,request):
        #如果方法中没有返回值（返回none），继续向后走
        #如果有返回值 HttpResponse，render，redirect


        #0.排除那些不需要登陆就能访问的页面
        if request.path_info == "/login/":
            return

        if request.path_info == "/index/":
            return

        if request.path_info == "/register/":
            return

        #1，读取当前访问用户的session信息，如果能读到已登录，继续向后走
        info_dict = request.session.get("info")
        if info_dict:
            return

        #2.没有登陆过，就跳转到登陆页面
        return redirect('/login/')