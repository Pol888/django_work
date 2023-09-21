from django.shortcuts import render
from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Привет, мир!')


def main_site(request):
    logger.info(f'Страничку main_site посетили {datetime.datetime.now()}')
    html = '''<!DOCTYPE html>
              <html lang="en">
              <head>
                  <meta charset="UTF-8">
                  <title>MI SITE!</title>
              </head>
              <body>
                  <h1>Мой первый сайт написанный с помощью фреймворка DJANGO</h1>
              </body>
              </html>'''
    return HttpResponse(html)


def about_me(request):
    logger.info(f'Страничку about_me посетили {datetime.datetime.now()}')
    html = '''<!DOCTYPE html>
                  <html lang="en">
                  <head>
                      <meta charset="UTF-8">
                      <title>MI SITE!</title>
                  </head>
                  <body>
                      <h1>Привет, это я!</h1>
                      <img src="/static/image/liar-liar.jpg">
                  </body>
                  </html>'''
    return HttpResponse(html)
