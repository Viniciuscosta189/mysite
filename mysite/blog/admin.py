from django.contrib import admin
from .models import Curso, Aluno

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "carga_horaria")
    search_fields = ("nome",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "curso", "matriculado_em")
    search_fields = ("nome", "email")
    list_filter = ("curso",)


# Register your models here.
