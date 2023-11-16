from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from django.db.models.query import QuerySet
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'main/index.html'

index = IndexView.as_view()

class AboutView(TemplateView):
    template_name = 'main/about.html'

about = AboutView.as_view()

class ContactView(TemplateView):
    template_name = 'main/contact.html'

contact = ContactView.as_view()

class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q', '')
        if q:
            queryset = Post.objects.filter(
                Q(title__icontains=q)
            )
        return queryset
    
post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'
    
post_detail = PostDetailView.as_view()