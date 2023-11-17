from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # 1.Todo 테이블의 내용물들을 다 읽어와서
    content = Todo.objects.all()
    # 2. 그것을 context에 넣은 뒤 html파일로 보내줌
    
    context = {
        'contents' : content
    }

    return render(request, 'todolist/index.html', context)

def add(request):
    content = request.GET.get('contents')
    # index.html의 input name이 contents니까 그걸 가져옴

    Todo.objects.create(content=content)
    # DB에 저장하기
    return redirect('todolist:index')
    # 얘를 redirect를 안하면 add/~~ 페이지로 넘어가서, 작업을 해놓은게 안보이는 페이지가 나옴
    # 리다이렉트로 원래페이지로 바로넘어가게 설정해주면 됨

def delete(request, pk):
    identity = Todo.objects.get(id=pk)
    identity.delete()
    return redirect('todolist:index')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    return render(request, 'todolist/create.html')

def edit(request):
    context = {
        'post' : post,
    }
    return render(request, 'todolist/edit.html', context)