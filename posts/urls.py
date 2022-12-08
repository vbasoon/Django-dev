from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('news/<int:news_id>', show_news, name='news'),
    path('category/<int:categories_id>', show_category, name='category'),
]
