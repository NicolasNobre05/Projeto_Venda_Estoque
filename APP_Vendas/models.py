from django.db import models
from APP_Cadastro.models import Produtos, Cliente, Funcionario 

class Venda(models.Model):
    cliente = models.ForeignKey('APP_Cadastro.Cliente', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('APP_Cadastro.Funcionario', on_delete=models.CASCADE)
    produtos = models.ManyToManyField('APP_Cadastro.Produtos') 
    valor_total = models.DecimalField(max_digits=10, decimal_places=2) 
    forma_pagamento = models.CharField(max_length=255, choices=[
        ('pix', 'Pix'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('dinheiro', 'Dinheiro'),
        ('combinado', 'Combinado')  
    ])  
    codigo_venda = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return f"Venda {self.codigo_venda} - {self.cliente.nome}"