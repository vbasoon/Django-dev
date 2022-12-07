from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'title': "Головна",
        'posts': news
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


def categories(request, cat_slug):
    return HttpResponse(f"<h1>Hовини за категоріями:</h1><p>{cat_slug}</p>")