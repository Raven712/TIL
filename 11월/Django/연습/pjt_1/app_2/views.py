from django.shortcuts import render
from .models import Article
# 현재폴더의 models에서 Article 가져오기 (DB 참고)

guestbook = []
# Create your views here.
def index(request):
    guestbook = Article.objects.all()
    # Select * FROM Articles
    context = {
        'guestbook' : guestbook
        # 'guestbook' : guestbook, 이것도 의미없어짐
        # DB에서 가져오기 하면 된다
    }
   
    return render(request, 'app_2/index.html', context)

def create(request):
    content = request.GET.get('content')
    Article.objects.create(content=content)
    context = {
        'content' : content,
        # 'guestbook' : guestbook.append(content), < 얘는 그냥 서버가 닫히면 리스트가 초기화 됨.
        # DB에 저장을 해야 영구적으로 남는다.
    }
    return render(request, 'app_2/create.html', context)