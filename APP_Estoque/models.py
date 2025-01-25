from django.db import models
from APP_Cadastro.models import Produtos, Lojas, Funcionario, Fornecedor

class RequisicaoCompra(models.Model):
    STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Pendente', 'Pendente'),
        ('Rejeitado', 'Rejeitado'),
    ]

    id_requisicao = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade_solicitada = models.IntegerField()
    solicitante = models.ForeignKey(Lojas, on_delete=models.CASCADE)  # Agora usa Lojas corretamente
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    coordenador_responsavel = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Requisição {self.id_requisicao} - {self.status}"
    
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('A', 'Aprovado'),
        ('P', 'Pendente'),
        ('R', 'Rejeitado'),
    ]
    requisicao = models.ForeignKey(RequisicaoCompra, on_delete=models.CASCADE) 
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    loja = models.ForeignKey(Lojas, on_delete=models.CASCADE) 
    data_pedido = models.DateField(auto_now_add=True)
    status_pedido = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Pedido {self.id} - {self.loja.nome} - {self.status_pedido}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'