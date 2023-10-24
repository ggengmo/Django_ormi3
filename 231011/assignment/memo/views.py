# memo > views.py
from django.shortcuts import render, redirect
from .models import Post
from django.db.models import Q
from .models import Post


def memo(request):
    if request.GET.get("q"):
        q = request.GET.get("q")
        db = Post.objects.filter(
            Q(title__icontains=q) | Q(contents__icontains=q)
        ).distinct()
    else:
        db = Post.objects.all()
    context = {
        "db": db,
    }
    return render(request, "memo/memo.html", context)


def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        "db": db,
    }
    return render(request, "memo/post.html", context)


def delete(request, pk):
    d = Post.objects.get(pk=pk)
    d.main_image.delete()
    d.delete()
    return redirect("memo")
