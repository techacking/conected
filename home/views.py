from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Cliente
from .models import Contato
from .models import Sala


@login_required
def home(request):
    return render(request, 'home.html')


# CBV ------------ ListView ---------------

class clienteList(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'

class contatoList(ListView):
    model = Contato
    template_name = 'clientes/contato_list.html'

class salaList(ListView):
    model = Sala
    template_name = 'clientes/sala_list.html'

# CBV -------------CreateView--------------

class clienteCreate(CreateView):
    model = Cliente
    fields = ['cnpj', 'inscricaoestadual', 'email', 'site', 'cep', 'endereco', 'numero', 'bairro', 'telefone', 'contato']
    template_name = 'clientes/cliente_form.html'

class contatoCreate(CreateView):
    model = Contato
    fields = ['nome', 'email', 'site', 'celular', 'telefone1', 'telefone2', 'foto']
    template_name = 'clientes/contato_form.html'

class salaCreate(CreateView):
    model = Sala
    fields = ['nome', 'capacidade', 'status', 'tipo']
    template_name = 'clientes/sala_form.html'

# CBV -------------UpgradeView--------------

class clienteAltera(UpdateView):
    model = Cliente
    fields = ['cnpj', 'inscricaoestadual', 'email', 'site', 'cep', 'endereco', 'numero', 'bairro', 'telefone', 'contato']
    template_name = 'clientes/cliente_update_form.html'

class contatoAltera(UpdateView):
    model = Contato
    fields = ['nome', 'email', 'site', 'celular', 'telefone1', 'telefone2', 'foto']
    template_name = 'clientes/contato_update_form.html'

class salaAltera(UpdateView):
    model = Sala
    fields = ['nome', 'capacidade', 'status', 'tipo']
    template_name = 'clientes/sala_update_form.html'

# CBV -------------DeleteView--------------

class clienteDeleta(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'


class contatoDeleta(DeleteView):
    model = Contato
    template_name = 'clientes/contato_confirm_delete.html'

class salaDeleta(DeleteView):
    model = Sala
    template_name = 'clientes/sala_confirm_delete.html'







