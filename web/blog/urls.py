from django.urls import path

from .views import create_blog

urlpatterns = [
    path('create/',create_blog, name='create-blog')
]