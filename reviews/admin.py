
""" reviews admin """
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ reviews admin fields """
    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'date_posted'
    )
