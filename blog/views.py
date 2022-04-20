from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.views import View

from .models import Blog, Category, Tag
from .forms import BlogForm


class BasicView:
    def category(self):
        categories = Category.objects.all()
        return categories

    def tag(self):
        tags = Tag.objects.all()
        return tags


class Home(BasicView, View):
    def get(self, request):
        context = {}
        context['blogs'] = Blog.objects.all()
        context['categories'] = self.category()
        context['tags'] = self.tag()

        return render(request, 'home.html', context)


class CategoryBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        category = Category.objects.get(slug=slug)
        context['category'] = category
        context['blogs'] = Blog.objects.filter(category=category)
        context['categories'] = self.category()
        context['tags'] = self.tag()

        return render(request, 'category_blogs.html', context)


class BlogCreate(BasicView,View):
    def get(self, request):
        context = {}
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['form'] = BlogForm()
        return render(request, 'blog_create.html', context)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.slug = slugify(form_create.title)
            form_create.user = request.user
            form_create.save()
            blog = Blog.objects.get(id=form_create.id)
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                tag, created = Tag.objects.get_or_create(name=tag.strip())
                blog.tags.add(tag)
            return redirect('home')
