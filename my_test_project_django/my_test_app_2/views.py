import datetime
from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from . import models


logger = logging.getLogger(__name__)


def create_publication(request):
    for i in range(5):
        autor = models.Autor(first_name=f'f_name{i}', last_name=f'l_name{i * 100}', email=f'gg{i}@mail.ru',
                             biography='biography' * (i * 100), birthday=datetime.date(1988, 8, 1 + i), )
        autor.save()
        for j in range(5):
            publication = models.Publication(heading='head' * j + (str(j) * 3),
                             content=str(j * i) + 'content' * (j * 10), autor=autor, category=models.Publication.category_st(i%2), )

            publication.save()
    return HttpResponse('create_ok')

def reading_publication(request):
    publications = models.Publication.objects.filter(autor__gt=10, autor__lt=13)
    for i in list(publications):
        i:models.Publication
        print(i.heading, i.publication_date, i.autor.pk, i.publish_flag, i.autor)

    return HttpResponse('read_ok')


def update_publication(request):
    publications = models.Publication.objects.all()
    for num, i in enumerate(publications):
        if num % 2 == 0:
            i:models.Publication
            i.publish_flag = True
            i.save()

    return HttpResponse('update_ok')


def delete_publication(request):
    publication = models.Publication.objects.filter(pk=10)
    if publication is not None:
        publication.delete()
    return HttpResponse('delete_ok')



def heads_and_tails(request):
    data = ['Орел', 'Решка']
    meaning = data[random.randint(0, 1)]
    logger.warning(f'Сработал маршрут task_5_1 и значение {meaning}')
    m = models.HeadsAndTailsDB(data=meaning)
    m.save()
    print(models.HeadsAndTailsDB.latest_results(10))
    return HttpResponse(f'{meaning}')

def cubic(request):
    meaning = random.randint(1, 6)
    logger.warning(f'Сработал маршрут task_5_2 и значение {meaning}')
    return HttpResponse(((f'{meaning}' + ', ') * meaning)[:-2])

def random_number(request):
    meaning = random.randint(1, 100)
    logger.warning(f'Сработал маршрут task_5_3 и значение {meaning}')
    return HttpResponse(f'{meaning}')