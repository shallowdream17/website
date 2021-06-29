#coding=utf-8
from django.contrib import admin
from django.urls import path

from djangoProject import views

urlpatterns=[
    #path('',views.test_login),
    #path('/login',views.test_slogin),
    path('',views.test_register),
]