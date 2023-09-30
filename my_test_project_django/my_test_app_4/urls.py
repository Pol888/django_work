from django.urls import path
from . import views

urlpatterns = [
    #path('/makes_a_choice/', views.makes_a_choice, name='makes_a_choice'),
    #path('/add_author/', views.add_author, name='add_author'),
    #path('/add_publication/', views.add_publication, name='add_publication'),
    #path('/add_a_comment_to_the_article/', views.add_a_comment_to_the_article, name='add_a_comment_to_the_article'),
    #path('/uninstall_or_update_the_product/', views.uninstall_or_update_the_product, name='uninstall_or_update_the_product'),
    #path('/products_editor/<int:id_process>/', views.products_editor, name='products_editor'),
    #path('/update_product/<int:id_product>/', views.update_product, name='update_product'),
    path('/add_product_home_work/', views.add_product_home_work, name='add_product_home_work'),
    ]