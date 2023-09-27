from django.urls import path
from . import views

urlpatterns = [
    path('/main_site/', views.main_site, name='main_site'),
    path('/about_me/', views.about_me, name='about_me'),
    path('/heads_and_tails/<int:count>/', views.heads_and_tails, name='heads_and_tails'),
    path('/cubic/<int:count>/', views.cubic, name='cubic'),
    path('/random_number/<int:count>/', views.random_number, name='random_number'),
    path('/authors_articles/<int:id_author>/', views.authors_articles, name='authors_articles'),
    path('/article/<int:id_publication>/', views.article, name='article'),
    path('/article_full_info/<int:id_publication>/', views.article_full_info, name='article_full_info'),
    path('/customer_orders/<int:id_customer>/', views.customer_orders, name='customer_orders'),
    path('/order_products/<int:id_order>/', views.order_products, name='order_products'),
    path('/customer_all_products/<int:id_customer>/', views.customer_all_products, name='customer_all_products'),
    path('/customer_all_products/<int:id_customer>/<int:id_process>', views.customer_all_products, name='customer_all_products'),
    ]