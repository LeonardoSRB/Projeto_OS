from django.db import models

class User (models.model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

class OrdemServico (models.Model):
    descricao = models.CharField(max_length=255)
    abertura = models.DateTimeField
    fechamento = models.DateTimeField
    patrimonio = models.ForeignKey
    ambiente = models.ForeignKey
    manutentor = models.ForeignKey
    prioridade = models.CharField(max_length=50)
    funcionario = models.CharField(max_length=255)
    sn_func = models.CharField(max_length=255)
    status = models.ForeignKey

class Patrimonios (models.Model):
    ni = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)


class Ambientes (models.Model):
    sig = models.IntegerField
    descricao = models.CharField(max_length=255)
    sn_resp = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)


class Funcionarios (models.Model):
    sn = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cargo = models.CharField(max_length=255)
    status = models.ForeignKey
    area = models.ForeignKey

class Area (models.Model):
    area = models.CharField(max_length=255)    

class Status (models.Model):
    status = models.CharField(max_length=100)