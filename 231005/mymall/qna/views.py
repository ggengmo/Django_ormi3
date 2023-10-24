from django.shortcuts import render


def qna(request):
    return render(request, "qna/qna.html")


def post(request, pk):
    return render(request, "qna/post.html")
