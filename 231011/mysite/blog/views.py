# blog > views.py
from django.shortcuts import render
from .models import Post


def blog(request):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

def test(request):
    return render(request, 'blog/test.txt')