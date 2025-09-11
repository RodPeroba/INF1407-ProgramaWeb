from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text="Entre o nome")
    idade = models.IntegerField(help_text="Entre a idade")
    salario = models.DecimalField(max_digits=8, decimal_places=2, help_text="Entre o salário")
    email = models.EmailField(help_text="Entre o email", max_length=254)
    telefone = models.CharField(max_length=20, help_text="Entre o telefone com DDD e DDI")
    dtNasc = models.DateField(help_text="Nascimento no formato DD/MM/AAAA", verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome