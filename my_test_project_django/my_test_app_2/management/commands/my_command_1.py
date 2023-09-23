import django.http.request as r
from django.core.management.base import BaseCommand
from ... import views

class Command(BaseCommand):
    help = 'task_5_sem_2'
    def add_arguments(self, parser):
        parser.add_argument('id_process', type=int, help='id in 1(c) or 2(r) or 3(u) or 4(d)')

    def handle(self, *args, **options):
        id_process = options['id_process']
        if id_process == 1:
            views.create_publication(request=r)
        elif id_process == 2:
            views.reading_publication(r)
        elif id_process == 3:
            views.update_publication(r)
        elif id_process == 4:
            views.create_publication(r)
        else:
            self.stdout.write('выберете значение от 1 до 4')



