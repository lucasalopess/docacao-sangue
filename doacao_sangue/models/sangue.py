from django.db import models


class Sangue(models.Model):
    id_sangue = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=2)
    fator_rh = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.tipo}{self.fator_rh}"


class Exame(models.Model):
    resultado_total = models.BooleanField(null=True, blank=True)
    exame_aids = models.BooleanField(null=True, blank=True)
    exame_sifilis = models.BooleanField(null=True, blank=True)
    exame_hepatite_a = models.BooleanField(null=True, blank=True)
    exame_hepatite_b = models.BooleanField(null=True, blank=True)
    sangue = models.OneToOneField(Sangue, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exames do sangue {self.sangue_id}"


class Estoque(models.Model):
    tipo_estoque = models.CharField(max_length=3)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo_estoque}: {self.quantidade}"
