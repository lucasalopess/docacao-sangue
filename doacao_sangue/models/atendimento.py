from django.db import models

from doacao_sangue.models.doador import Doador
from doacao_sangue.models.funcionario import Funcionario


class Atendimento(models.Model):
    protocolo = models.AutoField(primary_key=True)
    data = models.DateField()
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atendimento {self.protocolo}"
