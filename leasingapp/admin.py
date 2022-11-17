from django.contrib import admin
from django import forms

from .models import *


# Register your models here.
@admin.register(Product)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name']\

@admin.register(Interest_Rate)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['get_product', 'get_duration_more_than', 'get_duration_less_than_or_equal', 'get_rate']
    def get_product(self, obj):
        return obj.product.name


    get_product.short_description = 'Название программы'

    def get_duration_more_than(self, obj):
        return obj.duration_more_than

    get_duration_more_than.short_description = 'Минимальный срок'
    def get_duration_less_than_or_equal(self, obj):
        return obj.duration_less_than_or_equal

    get_duration_less_than_or_equal.short_description = 'Максимальный срок'
    def get_rate(self, obj):
        return obj.rate

    get_rate.short_description = 'Ставка'



@admin.register(Promo)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['get_product', 'get_description']
    def get_product(self, obj):
        return obj.product.name

    get_product.short_description = 'Название программы'  # Renames column head

    def get_description(self, obj):
        return obj.description

    get_description.short_description = 'Описание'

    def label_from_instance(self, obj):
        return "Product: {}".format(obj.product.name)


