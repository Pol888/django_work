from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    help = 'task_7_sem_2'

    @staticmethod
    def f_1(name_autor, quantity):
        autor = models.Autor.objects.filter(first_name=name_autor).first()
        publications = models.Publication.objects.filter(autor=autor)
        publications = list(sorted(publications, key=lambda x:x.heading))
        return publications[0: quantity]
    @staticmethod
    def f_2(name_autor, quantity):
        autor = models.Autor.objects.filter(first_name=name_autor).first()
        comments = models.Comment.objects.filter(autor=autor)
        comments = list(sorted(comments, key=lambda x: x.date_update))
        return comments[0: quantity]
    @staticmethod
    def f_3(heading, quantity):
        publication = models.Publication.objects.filter(heading=heading).first()
        comments = models.Comment.objects.filter(publication=publication)
        comments = list(sorted(comments, key=lambda x: x.date_update))
        return comments[0: quantity]

    def add_arguments(self, parser):
        parser.add_argument('id_process', type=int, help='id in 1(search_1) or 2(search_2) or 3(search_3)')
        parser.add_argument('argument_in_search', type=str)
        parser.add_argument('quantity', type=int)
    def handle(self, *args, **options):
        id_process = options['id_process']
        argument_in_search = options['argument_in_search']
        quantity = options['quantity']
        if id_process == 1:
            for i in self.f_1(argument_in_search, quantity):
                print(i)
        elif id_process == 2:
            for i in self.f_2(argument_in_search, quantity):
                print(i)
        elif id_process == 3:
            for i in self.f_3(argument_in_search, quantity):
                print(i)
        else:
            self.stdout.write('Неверный параметр')