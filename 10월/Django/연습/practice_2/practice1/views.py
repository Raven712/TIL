from django.shortcuts import render
  
# Create your views here.
def index(request):
    context = {
      
    }
    return render(request, 'index.html', context)

def pong(request):
    name = request.GET.get('ball')
    context = {
        'name' : name,
    }
    return render(request, 'pong.html', context)