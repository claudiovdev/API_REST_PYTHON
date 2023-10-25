from rest_framework import serializers
from escola.models import Aluno, Curso


class AlunoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
