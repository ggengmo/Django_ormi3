from django.shortcuts import render


def product(request):
    return render(request, "product/product.html")


def post(request, pk):
    return render(request, "product/post.html")
