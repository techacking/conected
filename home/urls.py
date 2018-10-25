from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [

    path('', home, name='home'),



    #CBV ---------------------ListView--------------------------------------

    path('cliente_list/', clienteList.as_view(), name='cliente_list'),
    path('contato_list/', contatoList.as_view(), name='contato_list'),
    path('sala_list/', salaList.as_view(), name='sala_list'),


    # CBV ---------------------CreateView-----------------------------------

    path('cliente_create/', clienteCreate.as_view(), name='cliente_create'),
    path('contato_create/', contatoCreate.as_view(), name='contato_create'),
    path('sala_create/', salaCreate.as_view(), name='sala_create'),

    # CBV ---------------------UpdateView-----------------------------------

    path('cliente_update/<int:pk>/', clienteAltera.as_view(), name='cliente_altera'),
    path('contato_update/<int:pk>/', contatoAltera.as_view(), name='contato_altera'),
    path('sala_update/<int:pk>/', salaAltera.as_view(), name='sala_altera'),

    # CBV ---------------------DeleteView-----------------------------------

    path('cliente_delete/<int:pk>/', clienteDeleta.as_view(), name='cliente_deleta'),
    path('contato_delete/<int:pk>/', contatoDeleta.as_view(), name='contato_deleta'),
    path('sala_delete/<int:pk>/', salaDeleta.as_view(), name='sala_deleta'),


]