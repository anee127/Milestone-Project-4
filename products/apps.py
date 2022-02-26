""" import for products app """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ products config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
