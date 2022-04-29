from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>', CategoryBlog.as_view(), name='category_blog'),
    path('tag/<slug:slug>', TagBlog.as_view(), name='tag_blog'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('update/<slug:slug>/', BlogUpdate.as_view(), name='update'),
]
