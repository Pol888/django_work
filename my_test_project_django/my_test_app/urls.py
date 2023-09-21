from django.urls import path
from . import views

urlpatterns = [
    path('/index/', views.index, name='index'),
    path('/main_site/', views.main_site, name='main_site'),
    path('/about_me/', views.about_me, name='about_me')
]