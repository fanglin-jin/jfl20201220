'''
定义当前子应用下的所有路由
Project: jfl20201220
Author: jinfanglin
Date: 2020/12/20
'''
from django.conf.urls import url
from . import views

urlpatterns = {
    # url(路径正则，视图函数的名字)
    url(r'^users/index/$',views.index),
}