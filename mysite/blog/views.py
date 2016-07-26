#coding=utf-8
from .models import BlogsPost
from django.shortcuts import render


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    context = {'blog_list':blog_list}
    return render(request,'blog/index.html',context)