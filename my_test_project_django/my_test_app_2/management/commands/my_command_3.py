from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    help = 'HOME_WORK'
    def add_arguments(self, parser):
        parser.add_argument('id_process', type=int, help='id in 1(create) or 2(read) or 3(search_3)')
    def handle(self, *args, **options):
        id_process = options['id_process']
        """Добавление покупателя и товаров"""
        if id_process == 1:   # Create


            #for i in range(50):
            #    customer = models.Customer(name=f'NAME {i}', email=f'fox{i}@in_tex.com',
            #                               number_phone=5543456453+i, address=f'street{i}')
            #    customer.save()
            #for i in range(50):
            #    product = models.Product(product_name=f'NAME_PROD {i}', comment=f'comment {i}',
            #                               price=10*i, count=2*i)
            #    product.save()
            #"""-----------------------------------------------"""
            #'''Один ко многим, добавление ордера и товаров к ордеру'''
            customers = models.Customer.objects.filter(pk=1).first()


            order = models.Order(customer=customers, order_amount=100.00)
            order.save()
            print(order)
            #product_1 = models.Product.objects.filter(pk=1).first()
            #product_2 = models.Product.objects.filter(pk=2).first()
            #product_3 = models.Product.objects.filter(pk=3).first()
#
            #summa_pds = product_1.price + product_2.price + product_3.price
#
            #order = models.Order(customer=customer, order_amount=summa_pds)
            #order.save()
#
            #prod_add_in_order_1 = models.ProductInOrder(order=order, product=product_1)
            #prod_add_in_order_2 = models.ProductInOrder(order=order, product=product_2)
            #prod_add_in_order_3 = models.ProductInOrder(order=order, product=product_3)
            #prod_add_in_order_1.save()
            #prod_add_in_order_2.save()
            #prod_add_in_order_3.save()
#
#
#
#
        elif id_process == 2: # Read
            for i in list(models.Order.objects.all()):
                i:models.Order
                products_in_order = models.ProductInOrder.objects.filter(order=i)
                print(i, products_in_order)


        elif id_process == 3: # update
            product = models.Product.objects.filter(pk=9).first()
            product.product_name = 'Яхта'
            print(product)
            product.save()
        elif id_process == 4: # delete
            product = models.Product.objects.filter(pk=10).first()
            if product is not None:
                product.delete()

        else:
            self.stdout.write('Неверный параметр')