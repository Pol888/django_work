from django.urls import path
from . import views

urlpatterns = [
    path('/task_5_1/', views.heads_and_tails, name='heads_and_tails'),
    path('/task_5_2/', views.cubic, name='cubic'),
    path('/task_5_3/', views.random_number, name='random_number'),
    path('/create_p/', views.create_publication, name='create_publication'),
    path('/read_p/', views.reading_publication, name='reading_publication'),
    path('/update_p/', views.update_publication, name='update_publication'),
    path('/delete_p/', views.delete_publication, name='delete_publication')
]