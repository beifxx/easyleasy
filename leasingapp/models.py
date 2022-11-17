from django.db import models
from django.contrib.auth.models import User
import json


class ClientProfile(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    type = models.CharField(max_length=100, default="Физлицо")
    # city = models.CharField(max_length=50)
    # street = models.CharField(max_length=50)
    # house_number = models.CharField(max_length=50)
    # apartment_number = models.CharField(max_length=50)
    # date_of_birth = models.DateField(blank=True, null=True)
    # id_card_num = models.CharField(max_length=9)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Support_Request(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateField()
    topic = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    phone_num = models.CharField(max_length=255, null=True)


class Document(models.Model):
    # id = models.AutoField(primary_key=True)
    definition = models.CharField(max_length=40)
    client_profile = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE)


# def products_to_choices():
#     choices = {}
#     products = Product.objects.all()
#     for product in products:
#         add = {
#             {
#                 'product_name': product.name,
#                 'product_id':product.id
#             }
#             }
#         choices.update(add)
#     print(json.loads(json.dumps(choices)))
#     return json.loads(json.dumps(choices))


class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    min_duration = models.IntegerField(verbose_name='Минимальная длительность')
    max_duration = models.IntegerField(verbose_name='Максимальна длительность')
    type = models.CharField(max_length=255, verbose_name='Вид лизинга')
    min_amount = models.FloatField(verbose_name='Минимальный размер')
    max_amount = models.FloatField(verbose_name='Максимальный размер')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
    def __str__(self):
        return self.name


class Application(models.Model):
    # id = models.AutoField(primary_key=True)
    client_profile = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE, null=True)
    date_applied = models.DateField(null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, null=True)


class Interest_Rate(models.Model):
    # id = models.AutoField(primary_key=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Программа')
    duration_more_than = models.IntegerField(verbose_name='Минимальный срок')
    duration_less_than_or_equal = models.IntegerField(verbose_name='Максимальный срок')
    rate = models.FloatField(verbose_name='Размер ставки')
    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'


class Promo(models.Model):
    # id = models.AutoField(primary_key=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Программа')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Acceptance_Rule(models.Model):
    # id = models.AutoField(primary_key=True)
    check_function = models.CharField(max_length=255)


class Product_Rule(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    rule = models.ForeignKey(to=Acceptance_Rule, on_delete=models.CASCADE)


class Deal(models.Model):
    # id = models.AutoField(primary_key=True)
    client_profile = models.ForeignKey(primary_key=True, to=ClientProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    duration = models.IntegerField()
    rate = models.FloatField()
    loan_amount = models.FloatField()
    regular_payment_size = models.FloatField()
    contract = models.ForeignKey(to=Document, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255)
    payment_by_deed = models.CharField(max_length=255, null=True)
    date_signed = models.DateField(null=True)
