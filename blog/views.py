from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Post, Category


def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def categories_views(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    tamplate_name = 'categories.html'
    return render(request, tamplate_name, context)


def categoryDelete_views(request, id):
    delete_category = get_object_or_404(Category, id=id)
    delete_category.delete()
    return redirect('/')


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    template_name = 'detail.html'
    return render(request, template_name, context)


@login_required(login_url='/login/')
def about(request):
    template_name = 'about.html'
    return render(request, template_name)


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username=username, password=password)

        if auth is not None:
            login(request, auth)
            return redirect('/about/')
        else:
            print("Sorry! Invalid Username And password")
    template_name = 'login.html'
    return render(request, template_name)


def logout_views(request):
    logout(request)
    return redirect(login_views)
