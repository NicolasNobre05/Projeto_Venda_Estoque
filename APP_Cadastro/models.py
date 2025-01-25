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

    def __str__(self):
        return self.nome
    
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

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=5)
    rua = models.CharField(max_length=200)
    numeroResidencial = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Lojas(models.Model):
    id_loja = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=5)
    rua = models.CharField(max_length=200)
    numeroResidencial = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()
    unidadeMedida = models.CharField(max_length=100)   

    def __str__(self):
        return f"{self.descricao} - {self.preco} - {self.unidadeMedida}"