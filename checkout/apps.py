""" import for checkout app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ checkout config """
    name = 'checkout'

    def ready(self):
        import checkout.signals
