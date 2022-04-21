""" reviews models """
from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """ review model for CRUD operations """

    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(choices=RATE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
