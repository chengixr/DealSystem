"""DealSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/list/', views.user_list),
    path('tpl/', views.tpl),
    # 请求和响应
    path('something/', views.something),

    # 用户登录
    path('', views.login),

    # 用户注册
    path('register/', views.register),

    # 债券信息
    path('secinfo/', views.secinfo),

    # 债券交易
    path('main/', views.main),
]
