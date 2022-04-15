""" import for product admin """
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ product admin fields """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ product admin diplayed name"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
