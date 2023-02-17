# Generated by Django 4.1.3 on 2023-02-16 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('date_launch', models.DateTimeField(verbose_name='Дата релиза')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Тип поставщика')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=255, verbose_name='Город')),
                ('debts', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Задолженность')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('products', models.ManyToManyField(related_name='providers', to='providers.product', verbose_name='Продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendors', to='providers.provider', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]
