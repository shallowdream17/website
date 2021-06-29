"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8080/page/2003
    #path('page/2003/',views.page_2003),
    path('',views.index),
    path('login',views.login),
    path('zhuanji',views.zhuanji),
    #path('jicheng',views.jicheng),
    #path('test_login',include('login.urls')),
    #path('test_register',include('register.urls')),
    #path('test_xianshi',views.show_view),
    path('register',views.register),
    path('active',views.user_active),
    path('logout',views.logout),
    path('yyh',views.yyh),
    path('shbk',views.shbk),
    path('wsrcxx',views.wsrcxx),
    path('sjmr',views.sjmr),
    path('songs',views.songs),
    path('my',views.mypage),
    path('changepwd',views.changepwd),
    #path('mycal',views.test_mycal),
    #path('page/1',views.page1_view),
    #path('page/2',views.page2_view),
    #path 转换器
    #path('page/<int:pg>',views.pg_view),

    #path('<int:a1>/<str:op>/<int:a2>',views.cal_view),
    #re_path(r'^(?P<a1>\d{1,2})/(?P<op>\w+)/(?P<a2>\d{1,2})$',views.cal2_view),

]
