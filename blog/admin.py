from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'date',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'statement',
        'date_added',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
