from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def notice(requset):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(requset, 'notice/notice.html', context)

def notice_post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'notice/post.html', context)
