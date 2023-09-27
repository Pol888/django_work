from django.shortcuts import render, get_object_or_404
import random
from . import models
from django.http import HttpResponse
import datetime

'''--------------------HOME WORK------------------------'''


def customer_all_products(request, id_customer, id_process=None):
    customer = get_object_or_404(models.Customer, pk=id_customer)
    list_date = [datetime.datetime.now() - datetime.timedelta(days=7), datetime.datetime.now() - datetime.timedelta(
        days=31), datetime.datetime.now() - datetime.timedelta(days=365), ]

    if id_process == 1 or id_process == 2 or id_process == 3:
        orders = list(models.Order.objects.filter(customer=customer, date_add__gte=list_date[id_process - 1]))
    elif id_process is None:
        orders = list(models.Order.objects.filter(customer=customer))
    else:
        raise Exception
    list_products = []
    for i in orders:
        for j in models.ProductInOrder.objects.filter(order=i):
            list_products.append(j.product)
    list_products = list(set(list_products))

    return render(request, 'my_test_app_3/home_work.html', {'list_products': list_products, 'id_customer': id_customer})
'''----------------------------------------------------------------------------------------------------------------------'''

def customer_orders(request, id_customer):
    customer = get_object_or_404(models.Customer, pk=id_customer)
    orders = list(models.Order.objects.filter(customer=customer))
    return render(request, 'my_test_app_3/task_7_orders.html', {'orders': orders})


def order_products(request, id_order):
    order = get_object_or_404(models.Order, pk=id_order)
    products = models.ProductInOrder.objects.filter(order=order)
    list_products = [i.product for i in products]
    print(list_products)
    return render(request, 'my_test_app_3/task_7_product.html', {'products': list_products})


# --------------------------------------------------------------------------------------------------------
def article_full_info(request, id_publication):
    publication = get_object_or_404(models.Publication, pk=id_publication)
    publication_upd = get_object_or_404(models.Publication, pk=id_publication)
    publication_upd.count_views = publication.count_views + 1
    publication_upd.save()
    return render(request, 'my_test_app_3/task_5.html', {'pub': publication})


def authors_articles(request, id_author):
    author = get_object_or_404(models.Autor, pk=id_author)
    publications = models.Publication.objects.filter(author=author)
    context = {'st': list(publications), 'au': author}
    return render(request, 'my_test_app_3/task_4.html', context)


def article(request, id_publication):
    publication = get_object_or_404(models.Publication, pk=id_publication)
    comments = models.Comment.objects.filter(publication=publication)
    return render(request, 'my_test_app_3/task_4_publication.html', {'pub': publication, 'cs': list(comments)})


# ------------------------------------------------------------------------------------------------------

def heads_and_tails(request, count):
    data = ['Орел', 'Решка']
    context = {'list_result': [data[random.randint(0, 1)] for _ in range(count)],
               'count': count}
    return render(request, 'my_test_app_3/task_3.html', context)


def cubic(request, count):
    context = {'list_result': [random.randint(1, 6) for _ in range(count)],
               'count': count}
    print(context.items())
    return render(request, 'my_test_app_3/task_3.html', context)


def random_number(request, count):
    random.randint(1, 100)
    context = {'list_result': [random.randint(1, 100) for _ in range(count)],
               'count': count}
    return render(request, 'my_test_app_3/task_3.html', context)


# -----------------------------------------------------------------------------------

def main_site(request):
    return render(request, 'my_test_app_3/main_task_1.html')


def about_me(request):
    return render(request, 'my_test_app_3/about_me.html')

# -----------------------------------------------------------------------------------
