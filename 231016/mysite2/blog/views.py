from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse


class PostList(ListView):
    model = Post
    ordering = "-pk"
    # template_name = 'blog/변경.html'


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostTest(DetailView):
    model = Post

    def get(self, request):
        return HttpResponse("PostTest get")

    def post(self, request):
        return HttpResponse("PostTest post")


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("postlist")


postlist = PostList.as_view()  # as_view는 진입 메소드
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()
