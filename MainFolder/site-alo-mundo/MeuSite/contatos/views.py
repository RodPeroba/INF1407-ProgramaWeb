from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.

class ContatoListView(View):

    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = {"pessoas": pessoas}
        return render(request, "contatos/listaContatos.html", contexto)


class ContatoDeleteView(View):

    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = {'pessoa': pessoa}
        return render(request, "contatos/confirmaExclusao.html", contexto)

class ContatoUpdateView(View):

    def get(self,request,pk,*args,**kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = {'form': ContatoModel2Form(instance=pessoa)}
        return render(request, "contatos/atualizaContato.html", contexto)
    
    def post(self,request,pk,*args,**kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {'form': formulario}
            return render(request, "contatos/atualizaContato.html", contexto)


class ContatoCreateView(View):

    def get(self, request, *args, **kwargs):
        contexto = {'form': ContatoModel2Form()}
        return render(request, "contatos/cadastroContato.html", contexto)
    
    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto = {
                'form': ContatoModel2Form,
                'mensagem': "Contato cadastrado com sucesso!"
            }
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {
                'form': formulario,
                'mensagem': "Erro ao cadastrar contato!"
            }
            return render(request, "contatos/cadastroContato.html", contexto)