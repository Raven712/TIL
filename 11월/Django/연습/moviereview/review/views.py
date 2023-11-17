from django.shortcuts import render
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
    return redner(request, 'review/detail.html', context)
# Create your views here.
