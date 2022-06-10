from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('posts', views.listar_posts , name='posts'),
    path('postar', views.postar, name='postar'),
    path('curtir/<id>', views.curtir, name='curtir')
]