# tube > views.py
from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def tubelist(request):
    posts = Post.objects.all()
    search = request.GET.get('q', '')
    if search:
        posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)
    return render(request, 'tube/tube_list.html', {'posts':posts})

def tubedetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data['message']
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, 'tube/tube_detail.html', {'post':post, 'form':form})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'tube/tube_list.html', {'posts':posts})

class TubeCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('tubelist')
    template_name = 'tube/tube_form.html'

class TubeUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('tubelist')
    template_name = 'tube/tube_form.html'

class TubeDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tubelist')
    template_name = 'tube/tube_confirm_delete.html'

write = TubeCreate.as_view()
edit = TubeUpdate.as_view()
delete = TubeDelete.as_view()