from django.db import models

from doacao_sangue.models.centro_doacao import CentroDoacao


class Funcionario(models.Model):
    cpf_func = models.CharField(max_length=14, unique=True)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    centro = models.ForeignKey(CentroDoacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpf_func


class Medico(Funcionario):
    crm = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"Médico {self.crm}"


class Enfermeiro(Funcionario):
    coren = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"Enfermeiro {self.coren}"
