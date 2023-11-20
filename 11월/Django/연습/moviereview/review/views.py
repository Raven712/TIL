from django.shortcuts import render, redirect
from .models import mo_re

def index(request):
    review = mo_re.objects.all()
    context = {
        'review' : review,
    }

    return render(request, 'review/index.html', context)

def detail(request, pk):
    article = mo_re.objects.get(pk=pk)
    context = {
        'article' : article,

    }
    return render(request, 'review/detail.html', context)

def new(request):
    return render(request, 'review/new.html')

def create(request):
    # new에서 title, content의 name을 가진 입력들을 가져온다
    title = request.GET.get('title')
    content = request.GET.get('content')
    # DB에 새로운 mo_re 저장하기
    mo_re.objects.create(
        title = title,
        content = content,
    )
    return redirect('review:index')

def delete(request, pk):
    article = mo_re.objects.get(pk=pk)
    article.delete()
    return redirect('review:index')
