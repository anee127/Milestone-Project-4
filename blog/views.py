from django.shortcuts import (
    render, reverse, redirect, get_object_or_404)
from .models import Blog


def blog(request):
    blogs = Blog.objects.all()
    template = 'blog/blog.html'

    context = {
        'blog': blogs,
    }
    return render(request, template, context)    