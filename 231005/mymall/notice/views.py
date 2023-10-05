from django.shortcuts import render

def notice(request):
    return render(request, 'notice/notice.html')

def free(request):
    return render(request, 'notice/free.html')

def free_detail(request, pk):
    return render(request, 'notice/free_detail.html')

def onenone(request):
    return render(request, 'notice/onenone.html')

def onenone_detail(request, pk):
    return render(request, 'notice/onenone_detail.html')