""" import for home views """
from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    print('hello')
    return render(request, 'home/index.html')
