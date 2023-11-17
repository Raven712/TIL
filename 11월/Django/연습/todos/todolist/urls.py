from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
]