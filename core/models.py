from django.db import models
from datetime import date

# Create your models here.

class Usuario(models.Model):

    nome = models.TextField(max_length=50)
    email = models.TextField(max_length=30)
    celular = models.TextField(max_length=25)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login = models.TextField(max_length=30, unique=True)
    senha = models.TextField(max_length=30)

class Coordenador(models.Model):
    pass

class Aluno(Usuario):
    
    ra = models.IntegerField()
    foto = models.TextField(max_length=255)

class Professor(Usuario):

    pass

class Disciplina(models.Model):

    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

class Curso(models.Model):
    pass

class DisciplinaOfertada(models.Model):

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')

class SolicitacaoMatricula(models.Model):
    pass

class Atividade(models.Model):

    pass

class AtividadeVinculada():

    pass

class EntregaAtividade():

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

class Mensagem(models.Model):

    pass