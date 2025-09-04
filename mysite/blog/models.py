from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="alunos")
    matriculado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Create your models here.
