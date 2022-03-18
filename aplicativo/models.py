from email.policy import default
from django.db import models

class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_materia

class Professor(models.Model):
    nome_professor = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_professor

class Genero(models.Model):
    genero_aluno = models.CharField(max_length=10)

    def __str__(self):
        return self.genero_aluno

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    ra_aluno = models.IntegerField(default=0, primary_key=True)
    data_nasc = models.DateField()
    genero_aluno = models.ForeignKey(Genero, on_delete=models.CASCADE)
    mae_aluno = models.CharField(max_length=200)
    pai_aluno = models.CharField(max_length=200)
    rua_aluno = models.CharField(max_length=200)
    numero_aluno = models.IntegerField(max_length=6)
    bairro_aluno = models.CharField(max_length=100)
    cidade_aluno = models.CharField(max_length=100)
    estado_aluno = models.CharField(max_length=100)

    class Meta:
            ordering = ['nome_aluno']

    def __str__(self):
        return str(self.nome_aluno)

class Registro(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nota_1_trim = models.FloatField(default=0)
    nota_2_trim = models.FloatField(default=0)
    nota_3_trim = models.FloatField(default=0)
    nota_4_trim = models.FloatField(default=0)
    relatorio_aluno = models.TextField()

    def __str__(self):
        return str(self.aluno) + ', ' + str(self.materia)

    def media(self):
        return (self.nota_1_trim + self.nota_2_trim + self.nota_3_trim + self.nota_4_trim) / 4