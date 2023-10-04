from django.contrib import admin
from .models import Customer, Product, Order, ProductInOrder, Autor, Publication, Comment

'''==================================HOME WORK================================'''


@admin.action(description='Сброс количества')
def counter_to_zero(modeladmin, request, queryset):
    queryset.update(count=0)



class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_reg']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Введите имя и фамилию'
    fieldsets = [
        ('Имя и Фамилия',
         {
             'classes': ['wide'],
             'fields': ['name'],
         },
         ),
        (
            'Личные данные',
            {
                'classes': ['collapse'],
                'description': 'Все данные клиента',
                'fields': ['email', 'number_phone', 'address'],
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'count']
    ordering = ['product_name']
    list_filter = ['price']
    actions = [counter_to_zero]
    readonly_fields = ['date_add']
    fields = ['product_name', 'comment', 'price', 'count', 'product_photo']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_amount', 'date_add']
    ordering = ['date_add']
    list_filter = ['customer']


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order']
    ordering = ['order']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)


'''--------------------------------------------------------------------------------------------'''
@admin.action(description='Флаг публикации "false"')
def set_flag_false(modeladmin, request, queryset):
    queryset.update(publish_flag=False)


@admin.action(description='Флаг публикации "true"')
def set_flag_true(modeladmin, request, queryset):
    queryset.update(publish_flag=True)


class AutorAdmin(admin.ModelAdmin):
    fields = ['last_name']
    list_display = ['first_name', 'email']
    ordering = ['last_name']
    search_fields = ['biography']
    search_help_text = 'Search for matches'


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['author', 'heading']
    ordering = ['publication_date']
    list_filter = ['publish_flag']
    actions = [set_flag_true, set_flag_false]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment']
    ordering = ['publication', 'date_update']
    readonly_fields = ['date_update']


admin.site.register(Autor, AutorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
