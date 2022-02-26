""" import for home app """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ home app config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
