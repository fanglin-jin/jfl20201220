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
    # 路由匹配的顺序是由上而下的，定义子路由时一定要在最后多加一个$
    url(r'^users/index/$',views.index),
}