from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about),
    path('contacts/', contacts),
    path('login/', login),
    path('register/', register),
    path('categories/', categories),
    path('categories/<str:cat_slug>', categories),
]
