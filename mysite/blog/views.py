#coding=utf-8

from .models import BlogsPost,Comment
from django.shortcuts import render
from django.http import Http404
from .forms import CommentForm

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all().order_by('-timestamp')
    context = {'blog_list':blog_list}
    return render(request,'blog/index.html',context)

def get_detail(request, blog_id):
    try:
        blog = BlogsPost.objects.get(id=blog_id)
    except BlogsPost.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-timestamp'),
        'form': form
    }
    return render(request, 'blog/blog-detail.html', ctx)