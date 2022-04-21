""" admin details for blog """
from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    """ blog Admin class """
    list_display = (
        'title',
        'content',
        'date',
    )


class CommentAdmin(admin.ModelAdmin):
    """ comment admin class """
    list_display = (
        'name',
        'statement',
        'date_added',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
