""" blog urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('edit_blog/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<slug:slug>/', views.delete_blog, name='delete_blog'),
]
