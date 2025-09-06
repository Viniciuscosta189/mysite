from django.contrib import admin
from .models import Curso, Aluno, Post

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "carga_horaria")
    search_fields = ("nome",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "curso", "matriculado_em")
    search_fields = ("nome", "email")
    list_filter = ("curso",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criado_em", "atualizado_em")
    search_fields = ("titulo", "conteudo")
    list_filter = ("criado_em",)

# Register your models here.
