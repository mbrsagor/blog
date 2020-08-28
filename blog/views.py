from django.shortcuts import render, get_object_or_404
from .models import Post,Category


def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def categories_views(request):
    categories = Category.objects.all()
    context = {"categories" : categories}
    tamplate_name = 'categories.html'
    return render(request,tamplate_name,context)



def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    template_name = 'detail.html'
    return render(request, template_name, context)


def about(request):
    template_name = 'about.html'
    return render(request, template_name)
