from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>', CategoryBlog.as_view(), name='category_blog'),
    path('create/', BlogCreate.as_view(), name='create')
]
