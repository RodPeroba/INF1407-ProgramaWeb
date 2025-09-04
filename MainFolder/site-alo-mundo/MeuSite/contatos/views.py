from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = {"pessoas": pessoas}
        return render(request, "pessoas/listaContatos.html", contexto)