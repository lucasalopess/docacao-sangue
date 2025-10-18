from django.contrib import admin

from doacao_sangue.models import *

admin.site.register(Doador)
admin.site.register(CentroDoacao)
admin.site.register(Funcionario)
admin.site.register(Medico)
admin.site.register(Enfermeiro)
admin.site.register(Hospital)
admin.site.register(Atendimento)
admin.site.register(Sangue)
admin.site.register(Exame)
admin.site.register(Estoque)
