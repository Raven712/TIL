from django.urls import path
from . import views

app_name = 'app_2'
urlpatterns = [
    path('', views.index, name='index'),
    path('app_2/create/', views.create, name='create'),
]