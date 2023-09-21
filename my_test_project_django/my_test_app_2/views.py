from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)


def heads_and_tails(request):
    data = ['Орел', 'Решка']
    meaning = data[random.randint(0, 1)]
    logger.warning(f'Сработал маршрут task_5_1 и значение {meaning}')
    return HttpResponse(f'{meaning}')

def cubic(request):
    meaning = random.randint(1, 6)
    logger.warning(f'Сработал маршрут task_5_2 и значение {meaning}')
    return HttpResponse(((f'{meaning}' + ', ') * meaning)[:-2])

def random_number(request):
    meaning = random.randint(1, 100)
    logger.warning(f'Сработал маршрут task_5_3 и значение {meaning}')
    return HttpResponse(f'{meaning}')