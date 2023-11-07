from django.urls import path
from . import views

# 메인페이지는 게시글의 목록 (R)
# 작성페이지는 따로 (C)
# 수정페이지도 따로 (U)

app_name = 'board'
urlpatterns = [
    path('', views.board, name='main'),
    path('write', views.write, name='write'),
    path('create', views.create, name='create')
]