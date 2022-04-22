from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.views import View

from .models import Blog, Category, Tag
from .forms import BlogForm, CommentForm


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

        return render(request, 'category_or_tag_blogs.html', context)


class BlogCreate(BasicView, View):
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


class TagBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        tag = Tag.objects.get(slug=slug)
        context['tag'] = tag
        context['blogs'] = Blog.objects.filter(tags=tag)
        context['categories'] = self.category()
        context['tags'] = self.tag()

        return render(request, 'category_or_tag_blogs.html', context)


class BlogDetail(BasicView, View):
    def get(self, request, slug):
        context = {}
        blog = Blog.objects.get(slug=slug)
        context['blog'] = blog
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['form'] = CommentForm()

        blog.views += 1
        blog.save()

        return render(request, 'blog_detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        blog = Blog.objects.get(slug=slug)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.blog = blog
            form_comment.user = request.user
            form_comment.save()
            return redirect('blog', blog.slug)
