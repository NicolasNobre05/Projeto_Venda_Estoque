from django.shortcuts import render
import requests
import json

# Create your views here.

def CadastroFornecedor(request):
    return render(request, 'CadastroFornecedor.html')

def CadastroLoja(request):
    
    return render(request, 'CadastroLoja.html')

def CadastroProduto(request):
    pessoas.Cadastro(request)
    return render(request, 'CadastroProduto.html')

def CadastroCliente(request):
    pessoas.Cadastro(request)
    return render(request, 'CadastroCliente.html')

def CadastroVendedor(request):
    return render(request, 'CadastroVendedor.html')



class pessoas:
    def __init__(self, nome,nascimento, idade):
        self.nome = nome
        self.nascimento = nascimento
        self.idade = idade
    
    def Cadastro(request):
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        pessoas.CalculoIdade(nascimento)

    def CalculoIdade(nascimento):


