from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = {"pessoas": pessoas}
        return render(request, "contatos/listaContatos.html", contexto)

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'form': ContatoModel2Form()}
        return render(request, "contatos/cadastroContato.html", contexto)