from django.shortcuts import render, redirect
from .models import board1
# DB의 이름과 view.py 내부의 함수이름이 같아버리면 오류가 생긴다 (board가 중첩이 되버렸음)


# Create your views here.
def board(request):
    # 여기서는 모든 글 목록을 보여줘야함
    # 1. DB에서 모든 글 불러오기
    posting = board1.objects.all()
    # 2. 템플릿에 보내주기, context 이하가 템플릿에 보내주는거임.

    context = {
        'posting' : posting,
    }
    return render(request, 'board/board.html', context)

def write(request):
    return render(request, 'board/write.html')

def create(request):
    # 1. 파라미터로 날아온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 2. DB에 저장
    board1.objects.create(title=title, content=content)
    # board를 불러오기위해 상단에 from .models(현재폴더의 models파일) 로 부터 DB를 import 해온다
    # board의 title 칼럼에 현재 함수에서 request.GET.get('title')을 해온 title을 할당시켜준것임

    context = {
        'title' : title,
        'content' : content,
    }
    return redirect('board:main')

def delete(request, pk):
    board1.objects.get(id=pk).delete()
    return redirect('board:main')