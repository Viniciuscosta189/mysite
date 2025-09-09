from django.test import TestCase
from .models import Curso, Aluno

class ModelsTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(nome="Matemática", descricao="Teste", carga_horaria=40)
        self.aluno = Aluno.objects.create(nome="Vinícius", email="vinicius@email.com", curso=self.curso)

    def test_curso_criado(self):  # precisa começar com 'test_'
        self.assertEqual(self.curso.nome, "Matemática")

    def test_aluno_criado(self):
        self.assertEqual(self.aluno.nome, "Vinícius")
