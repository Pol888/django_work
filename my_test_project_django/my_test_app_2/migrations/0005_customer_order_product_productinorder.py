# Generated by Django 4.2.5 on 2023-09-23 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_app_2', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number_phone', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('date_reg', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_test_app_2.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('comment', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_test_app_2.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_test_app_2.product')),
            ],
        ),
    ]
