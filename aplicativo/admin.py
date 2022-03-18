from django.contrib import admin
from .models import Aluno, Professor, Materia, Registro, Genero

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Registro)
admin.site.register(Genero)


