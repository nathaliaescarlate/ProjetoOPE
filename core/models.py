from django.db import models
from datetime import date

# Create your models here.

class Usuario(models.Model):

    nome = models.TextField(max_length=50)
    email = models.TextField(max_length=30)
    celular = models.TextField(max_length=25)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login = models.TextField(max_length=30, unique=True)
    senha = models.TextField(max_length=8) #TIRAR OU NÃO O CHECK??? PROF NÃO DEU EM AULA

class Coordenador(models.Model):
    pass

class Aluno(models.Model):
    
    nome = models.TextField(max_length=50)
    email = models.TextField(max_length=50, unique=True)
    celular = models.TextField(max_length=11, unique=True)
    ra = models.TextField(max_length=7, unique=True)
    foto = models.TextField(max_length=100)

class Professor(Usuario):
    nome = models.TextField(max_length=50)
    email = models.TextField(max_length=30)
    celular = models.TextField(max_length=11)
    apelido = models.TextField(max_length=50)

    idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Disciplina(models.Model):
    
    nome = models.TextField(max_length=30, unique=True)
    data = models.DateField(default=date(year=1900, month=1, day=1))
    status = models.TextField(max_length=10)
    plano_ensino = models.TextField(max_length=1000)
    carga_horaria = models.SmallIntegerField()
    competencias = models.TextField(max_length=1000)
    habilidades = models.TextField(max_length=1000)
    ementa = models.TextField(max_length=1000)
    conteudo_programatico = models.TextField(max_length=1000)
    bibliografia_basica = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    percentual_pratico = models.SmallIntegerField()
    percentual_teorico = models.SmallIntegerField()
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

class Curso(models.Model):

    curso = models.TextField(max_length=50)
    
class DisciplinaOfertada(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    class Meta:
       unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')

class SolicitacaoMatricula(models.Model):
    
    #dtsolicitacao = models.datetime
    status = models.TextField(max_length=15)

    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    iddisciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    idcoordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

class Atividade(models.Model):

    titulo    = models.TextField(max_length=30) 
    descricao = models.TextField(max_length=100) 
    conteudo  = models.TextField(max_length=8000) 
    tipo      = models.TextField(max_length=15) 
    extras    = models.TextField(max_length=100) 
    
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
     

class AtividadeVinculada():

    atividade     = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    professor     = models.ForeignKey(Professor, on_delete=models.PROTECT)
    dofertada     = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

    rotulo        = models.TextField(max_length=500)  
    status        = models.TextField(max_length=15)
    dtiniresposta = models.DateTimeField()
    dtfimresposta = models.DateTimeField()


class EntregaAtividade():

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

class Mensagem(models.Model):
 
    aluno      = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    professor  = models.ForeignKey(Professor, on_delete=models.PROTECT)

    assunto    = models.TextField(max_length=100) 
    referencia = models.TextField(max_length=100) 
    conteudo   = models.TextField(max_length=500) 
    status     = models.TextField(max_length=50) 
    dtenvio    = models.DateField(default=date(year=1900, month=1, day=1))
    dtresposta = models.DateField(default=date(year=1900, month=1, day=1))
    resposta   = models.TextField(max_length=500)



