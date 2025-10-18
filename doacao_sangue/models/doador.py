from django.db import models


class Doador(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=16)
    rua = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
