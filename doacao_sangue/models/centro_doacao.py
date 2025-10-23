from django.db import models

from doacao_sangue.models.hospital import Hospital


class CentroDoacao(models.Model):
    id_centro = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    numero = models.PositiveIntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="centros_doacao")


    def __str__(self):
        return f"Centro {self.id_centro}"
