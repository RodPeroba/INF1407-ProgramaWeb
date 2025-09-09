from django.urls import path
from contatos.views import ContatoListView, ContatoCreateView

app_name = "contatos"

urlpatterns = [
    path("lista/", ContatoListView.as_view(), name="lista-contatos"),   
    path("cria/", ContatoCreateView.as_view(), name="cria-contato"),
    ]