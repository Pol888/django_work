import datetime

from django import forms
#from .models import Autor as AuthorModel, Publication as PublicationModel, Product


#--------------------------------------------------------------------------------------------
#class StaticFunctionsForForms():
#    @staticmethod
#    def list_of_authors():
#        return [(str(i.id), f'{i.first_name} {i.last_name}') for i in AuthorModel.objects.all()]
#
#    @staticmethod
#    def list_of_products():
#        return [(str(i.id), i.product_name) for i in Product.objects.all()]

#----------------------------------------------------------------------------------------------



class ProductCreate(forms.Form):
    product_name = forms.CharField(max_length=250)
    comment = forms.CharField(max_length=2000)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    product_photo = forms.ImageField()


#class ProductUpdate(forms.Form):
#    product_name = forms.ChoiceField(choices=StaticFunctionsForForms.list_of_products())


#--------------------------------------------------------------------------------------------
#class ChoosingAnApp(forms.Form):
#    choice = forms.ChoiceField(choices=[('A', 'Монетка'), ('B', 'Кость'), ('C', 'Число')])
#    attempts = forms.IntegerField(min_value=1, max_value=64)
#
#
#
#class Autor(forms.Form):
#    first_name = forms.CharField(max_length=100)
#    last_name = forms.CharField(max_length=100)
#    email = forms.EmailField()
#    biography = forms.CharField()
#    birthday = forms.DateField(initial=datetime.date.today())





#class Publication(forms.Form):
#    heading = forms.CharField(max_length=200)
#    content = forms.CharField()
#    author = forms.ChoiceField(choices=StaticFunctionsForForms.list_of_authors())
#    category = forms.ChoiceField(choices=[(PublicationModel.category_st(0), PublicationModel.category_st(0)), (PublicationModel.category_st(1), PublicationModel.category_st(1))])
#
#
#class Comment(forms.Form):
#    comment = forms.CharField(max_length=1000)



