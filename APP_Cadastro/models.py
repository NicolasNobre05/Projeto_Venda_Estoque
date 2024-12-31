from django.db import models

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=5)
    rua = models.CharField(max_length=200)
    numeroResidencial = models.CharField(max_length=100, null=True)
    

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=5,)
    rua = models.CharField(max_length=200)
    numeroResidencial = models.CharField(max_length=100, null=True)