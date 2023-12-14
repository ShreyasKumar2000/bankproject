from django.urls import path
from .views import home, user_logout, new_page, forms, lastpage, get_cities

urlpatterns = [
    path('', home, name='home'),

    path('new_page/', new_page, name='new_page'),

    path('logout/', user_logout, name='logout'),
path('forms',forms,name='forms'),
    path('lastpage',lastpage,name='lastpage'),
    path('get_cities/',get_cities,name='get_cities'),]
