from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('postar', views.postar, name='postar'),
    path(r'^curtir/$', views.curtir, name='curtir')
]