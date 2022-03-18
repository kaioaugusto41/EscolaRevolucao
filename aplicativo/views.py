from django.shortcuts import get_object_or_404, render
from .models import Aluno, Registro, Genero

nota1 = Registro

def index(request):
    dados = {
        'alunos': Aluno.objects.all(),
        'generos': {
            'masculino': Genero.objects.get(id=1),
            'feminino': Genero.objects.get(id=2)
        }
    }
    return render(request, 'index.html', dados)

def aluno(request, aluno_ra_aluno):

    dados = {
        'aluno' : get_object_or_404(Aluno, pk=aluno_ra_aluno),
        'registro': Registro.objects.filter(aluno=aluno_ra_aluno),
        'generos': {
            'masculino': Genero.objects.get(id=1),
            'feminino': Genero.objects.get(id=2)
        },
    }


    return render(request, 'aluno.html', dados)