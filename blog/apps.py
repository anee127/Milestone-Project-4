""" blog app """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ blog configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
