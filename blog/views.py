from django.shortcuts import render
from django.views import View

from .models import Blog, Category


class Home(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'home.html', context)


class CategoryBlog(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        blogs = Blog.objects.filter(category=category)
        context = {
            'category': category,
            'blogs': blogs
        }
        return render(request, 'category_blogs.html', context)