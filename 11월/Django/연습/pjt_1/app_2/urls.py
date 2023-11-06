from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app_2/create/', views.create),
]