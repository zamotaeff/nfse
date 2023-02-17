from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=255)
    model = models.CharField(verbose_name='Модель',
                             max_length=255)
    date_launch = models.DateTimeField(verbose_name='Дата релиза',
                                       auto_now=False,
                                       auto_now_add=False,
                                       blank=True,
                                       null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Provider(models.Model):
    """
    Модель поставщика имеет собственный тип
    """
    TYPES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    type = models.SmallIntegerField(verbose_name='Тип поставщика',
                                    choices=TYPES)

    title = models.CharField(verbose_name='Название',
                             max_length=255,
                             unique=True)
    email = models.EmailField(verbose_name='Email',
                              unique=True)
    country = models.CharField(verbose_name='Страна',
                               max_length=255)
    city = models.CharField(verbose_name='Город',
                            max_length=255)
    street = models.CharField(verbose_name='Улица',
                              max_length=255)
    house_number = models.CharField(verbose_name='Номер дома',
                                    max_length=255)
    debts = models.DecimalField(verbose_name='Задолженность',
                                decimal_places=2,
                                max_digits=20,
                                default=0)
    date_created = models.DateField(auto_now_add=True,
                                    verbose_name='Дата создания')
    products = models.ManyToManyField(Product,
                                      verbose_name='Продукты',
                                      related_name='providers',
                                      null=True,
                                      blank=True)
    provider = models.ForeignKey('self',
                                 on_delete=models.SET_NULL,
                                 verbose_name='Поставщик',
                                 related_name='vendors',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
