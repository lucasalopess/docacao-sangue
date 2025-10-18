from django.db import models


class CentroDoacao(models.Model):
    id_centro = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f"Centro {self.id_centro}"
