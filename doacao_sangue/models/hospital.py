from django.db import models


class Hospital(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    nome = models.CharField(max_length=50)
    rua = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
