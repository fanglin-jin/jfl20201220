from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """
    视图函数，至少有一个参数来接收请求对象
    :param request:
    :return: 响应对象HttpReponse
    """
    return HttpResponse("hello world!!!")