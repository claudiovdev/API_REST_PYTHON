from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerealizer,CursoSerealizer

class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos alunos e alunas"""
    queryset = Aluno.objects.all()
    serealizer_class = AlunoSerealizer

class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serealizer_class = CursoSerealizer
