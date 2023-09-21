from django.urls import path
from . import views

urlpatterns = [
    path('/task_5_1/', views.heads_and_tails, name='heads_and_tails'),
    path('/task_5_2/', views.cubic, name='cubic'),
    path('/task_5_3/', views.random_number, name='random_number')
]