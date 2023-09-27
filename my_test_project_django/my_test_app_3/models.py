from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_phone = models.IntegerField()
    address = models.CharField(max_length=150)
    date_reg = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    comment = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.product_name}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product)
    order_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order - {self.pk}, {self.date_add}, {self.customer}, sum - {self.order_amount}'

class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return f' {self.product}'
#--------------------------------------------------------------------------------------------------
class Autor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()
    def __str__(self):
        return f'Autor {self.first_name}, {self.last_name}, {self.email}, {self.birthday}.'


class Publication(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    publish_flag = models.BooleanField(default=False)
    def __str__(self):
        return f'heading {self.heading}, count_views {self.count_views}, publish_flag {self.publish_flag}'

    @staticmethod
    def category_st(category):
        list_category = ['norm', 'super']
        return list_category[category]



class Comment(models.Model):
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment - {self.author}, {self.comment}, {self.date_update}'
