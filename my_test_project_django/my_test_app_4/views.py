from django.shortcuts import render, get_object_or_404
import random
from  .forms import ProductCreate
from  .models import Product
#from .forms import ChoosingAnApp, Autor, Publication, Comment, ProductCreate#, #ProductUpdate
#from .models import Autor as AuthorModel, Publication as PublicationModel, Comment as CommentModel, \
    #Product as ProductModel
from django.core.files.storage import FileSystemStorage

'''HOME WORK'''

def add_product_home_work(request):
        form = ProductCreate()
        massage = 'Введите данные, выберете фото'
        button_name = 'Добавить'
        if request.method == 'POST':
            form = ProductCreate(request.POST, request.FILES)
            if form.is_valid():
                product_name = form.cleaned_data['product_name']
                comment = form.cleaned_data['comment']
                price = form.cleaned_data['price']
                count = form.cleaned_data['count']
                product_photo = form.cleaned_data['product_photo']
                #fs = FileSystemStorage()
                #fs.save(product_photo.name, product_photo)

                Product(product_name=product_name, comment=comment, price=price, count=count,
                            product_photo=product_photo).save()
                massage = 'Данные загружены'
        context = {'form': form, 'massage': massage, 'button_name': button_name}
        return render(request, 'my_test_app_4/add_product.html', context)
'''----------------------------------------------------------------------------------'''
#-------------------------------------------------------------------------------------------------
#def uninstall_or_update_the_product(request):
#    return render(request, 'my_test_app_4/uninstall_or_update_the_product.html')
#
#def products_editor(request, id_process=None):
#    global form, massage, product_id
#    button_name = ['Добавить', 'Изменить']
   #if len(products_editor.__dict__) != 0:
   #    if request.method == 'POST':
   #        form = ProductCreate(request.POST)
   #        if form.is_valid():
   #            product = ProductModel.objects.filter(pk=products_editor.__dict__['product_id']).first()
   #            print(product)
   #            product_name = form.cleaned_data['product_name']
   #            comment = form.cleaned_data['comment']
   #            price = form.cleaned_data['price']
   #            count = form.cleaned_data['count']
   #            product.product_name = product_name
   #            product.comment = comment
   #            product.price = price
   #            product.count = count
   #            product.save()
   #            products_editor.__dict__.clear()
   #            return render(request, 'my_test_app_4/end.html')


    #if id_process == 1:
    #    form = ProductCreate()
    #    massage = 'Введите данные'
    #    button_name = button_name[0]
    #    if request.method == 'POST':
    #        form = ProductCreate(request.POST, request.FILES)
    #        if form.is_valid():
    #            product_name = form.cleaned_data['product_name']
    #            comment = form.cleaned_data['comment']
    #            price = form.cleaned_data['price']
    #            count = form.cleaned_data['count']
    #            ProductModel(product_name=product_name, comment=comment, price=price, count=count,
    #                         ).save()
    #            massage = 'Данные загружены'

    #elif id_process == 2:
    #    form = ProductUpdate()
    #    massage = 'Выберете продукт'
    #    button_name = button_name[1]
    #    if request.method == 'POST':
    #        form = ProductUpdate(request.POST)
    #        if form.is_valid():
    #            product_id = int(form.cleaned_data['product_name'])
    #            product = ProductModel.objects.filter(pk=product_id).first()
    #            product_str = f'|{product.product_name}, {product.comment}, {product.price}, {product.count}|'
    #            form = ProductCreate()
    #            massage = 'Измените данные'
    #            products_editor.__dict__['product_id'] = product_id
#
    #            return render(request, 'my_test_app_4/update product.html', {'form': form, 'massage': massage, 'product_str': product_str})
#
#    context = {'form': form, 'massage': massage, 'button_name': button_name}
#    return render(request, 'my_test_app_4/add_product.html', context)


#-----------------------------------------------------------------------------------------------
#def add_a_comment_to_the_article(request, id_publication=1):
#    publication = get_object_or_404(PublicationModel, pk=id_publication)
#    comments = CommentModel.objects.filter(publication=publication)
#    massage = 'Добавить комментарий'
#    form = Comment()
#    if request.method == 'POST':
#        form = Comment(request.POST)
#        if form.is_valid():
#            comment = form.cleaned_data['comment']
#            CommentModel(author=AuthorModel.objects.filter(pk=1).first(), publication=publication, comment=comment).save()
#            request.method = 'GET'
#            return add_a_comment_to_the_article(request)
#    context = {'publication': publication, 'comments': comments, 'form': form, 'massage': massage}
#    return render(request, 'my_test_app_4/task_5_publication_for_add_comment.html', context)



#def add_publication(request):
#    massage = None
#    if request.method == 'POST':
#        form = Publication(request.POST)
#        if form.is_valid():
#            heading = form.cleaned_data['heading']
#            content = form.cleaned_data['content']
#            author = form.cleaned_data['author']
#            category = form.cleaned_data['category']
#            PublicationModel(heading=heading, content=content, author=AuthorModel.objects.
#                             filter(pk=int(author)).first(), category=category).save()
#            massage = 'Данные приняты'
#    else:
#        form = Publication()
#        massage = 'Введите данные о статье'
#
#    return render(request, 'my_test_app_4/add_author.html', {'form': form, 'massage': massage})




#def add_author(request):
#    massage = None
#    if request.method == 'POST':
#        form = Autor(request.POST)
#        if form.is_valid():
#            first_name = form.cleaned_data['first_name']
#            last_name = form.cleaned_data['last_name']
#            email = form.cleaned_data['email']
#            biography = form.cleaned_data['biography']
#            birthday = form.cleaned_data['birthday']
#            author = AuthorModel(first_name=first_name, last_name=last_name, email=email, biography=biography,
#                                 birthday=birthday)
#            author.save()
#            massage = 'Данные приняты'
#    else:
#        form = Autor()
#        massage = 'Введите данные автора'
#
#    return render(request, 'my_test_app_4/add_author.html', {'form': form, 'massage': massage})
#-----------------------------------------------------------------------------------
#def makes_a_choice(request):
#    if request.method == 'POST':
#        form = ChoosingAnApp(request.POST)
#        if form.is_valid():
#            choice = form.cleaned_data['choice']
#            attempts = form.cleaned_data['attempts']
#            if choice == 'A':
#                return heads_and_tails(request, attempts)
#            elif choice == 'B':
#                return cubic(request, attempts)
#            elif choice == 'C':
#                return random_number(request, attempts)
#    else:
#        form = ChoosingAnApp()
#    return render(request, 'my_test_app_4/make_a_choice.html', {'form': form})
#
#
#def heads_and_tails(request, count):
#    data = ['Орел', 'Решка']
#    context = {'list_result': [data[random.randint(0, 1)] for _ in range(count)],
#               'count': count}



#    return render(request, 'my_test_app_4/task_1_apps.html', context)


#def cubic(request, count):
#    context = {'list_result': [random.randint(1, 6) for _ in range(count)],
#               'count': count}
#    print(context.items())
#    return render(request, 'my_test_app_4/task_1_apps.html', context)
#
#
#def random_number(request, count):
#    random.randint(1, 100)
#    context = {'list_result': [random.randint(1, 100) for _ in range(count)],
#               'count': count}
#    return render(request, 'my_test_app_4/task_1_apps.html', context)
