from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'title': "Головна",
        'posts': news,
        'categories': categories,
        'category_selected': 0
    }
    return render(request, 'posts/index.html', context)


def about(request):
    context = {
        'title': "About",
    }
    return render(request, 'posts/about.html', context)


def contacts(request):
    context = {
        'title': "Contacts",
    }
    return render(request, 'posts/contacts.html', context)


def login(request):
    context = {
        'title': "Login",
    }
    return render(request, 'posts/login.html', context)


def register(request):
    context = {
        'title': "Register",
    }
    return render(request, 'posts/register.html', context)


def blankPage(request, exception):
    return HttpResponseNotFound("<h1>Новини відсутні</h1>")

def show_news(request, news_id):
    return HttpResponse(f"<h1>Hовина з id:</h1><p>{news_id}</p>")


def show_category(request, categories_id):
    news = News.objects.filter(categories_id=categories_id)
    categories = Category.objects.all()

    if len(news) == 0:
        raise Http404()

    context = {
        'title': "Новини за категорією",
        'posts': news,
        'categories': categories,
        'category_selected': categories_id
    }
    return render(request, 'posts/index.html', context)
