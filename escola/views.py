from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer  import AlunoSerializer,CursoSerializer, MatriculaSerializer


class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer