import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from django.shortcuts import render
from utils.tratamento_dados import data_menor
import requests
from datetime import datetime
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def CadastroFornecedor(request):
    return render(request, 'CadastroFornecedor.html')

def CadastroLoja(request):
    
    return render(request, 'CadastroLoja.html')

def CadastroProduto(request):
    return render(request, 'CadastroProduto.html')

def CadastroCliente(request):
    if request.method == 'POST':
        #INFORMAÇÕES DO CLIENTE
        Cliente_info = pessoas.Cadastro(request)
        novo_cliente = Cliente()
        novo_cliente.cpf =  Cliente_info.CPF
        novo_cliente.nome = Cliente_info.nome
        novo_cliente.dataNascimento = Cliente_info.nascimento
        novo_cliente.idade = Cliente_info.idade
        novo_cliente.email = Cliente_info.email
        novo_cliente.telefone = Cliente_info.telefone
        novo_cliente.cep = Cliente_info.cep
        novo_cliente.estado = Cliente_info.estado
        novo_cliente.cidade = Cliente_info.cidade
        novo_cliente.bairro = Cliente_info.bairro
        novo_cliente.rua = Cliente_info.rua
        novo_cliente.numeroResidencial = Cliente_info.numeroResidencial
        novo_cliente.save()

    return render(request, 'cliente.html')

def CadastroVendedor(request):
    if request.method == 'POST':
        funcionario_info = pessoas.Cadastro(request)
        novo_vendedor = Funcionario()
        novo_vendedor.cpf =  funcionario_info.CPF
        novo_vendedor.nome = funcionario_info.nome
        novo_vendedor.dataNascimento = funcionario_info.nascimento
        novo_vendedor.idade = funcionario_info.idade
        novo_vendedor.email = funcionario_info.email
        novo_vendedor.telefone = funcionario_info.telefone
        novo_vendedor.cep = funcionario_info.cep
        novo_vendedor.estado = funcionario_info.estado
        novo_vendedor.cidade = funcionario_info.cidade
        novo_vendedor.bairro = funcionario_info.bairro
        novo_vendedor.rua = funcionario_info.rua
        novo_vendedor.numeroResidencial = funcionario_info.numeroResidencial
        novo_vendedor.save()

    return render(request, 'CadastroVendedor.html')



class pessoas:
    def __init__(self, CPF, nome,nascimento, idade,email,telefone,cep,estado,cidade,bairro,rua,numeroResidencial):
        self.CPF = CPF
        self.nome = nome
        self.nascimento = nascimento
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numeroResidencial = numeroResidencial

    def __str__(self):
        return f'Pessoa(CPF={self.CPF}, Nome={self.nome}, Nascimento={self.nascimento}, Idade={self.idade}, Email={self.email}, Telefone={self.telefone}, CEP={self.cep}, Estado={self.estado}, Cidade={self.cidade}, Bairro={self.bairro}, Rua={self.rua}, NumeroResidencial={self.numeroResidencial})'
    
    def Cadastro(request):

        CPF = request.POST.get('CPF')
        nascimento = request.POST.get('nascimento')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numeroResidencial = request.POST.get('numeroResidencial')
        
        #CONFERIR SE A DATA DE NASCIMENTO É MENOR QUE A DATA ATUAL
        if data_menor(nascimento) == False:
            return False
        
        #PEGAR SITUAÇÃO DO CPF E NOME DO CLIENTE
        dados_API_CPF = pessoas.APICPF(CPF,nascimento)
        pessoa_info = dados_API_CPF['data'][0]
        nome = pessoa_info.get('nome')
        ano_obito = pessoa_info.get('ano_obito')
        if ano_obito != None:
            return False
        
        #PEGER NOME DA CIDADE/ESTADO E BAIRRO

        dados_API_CEP = pessoas.APICEP(cep)
        cep_info = dados_API_CEP['data'][0]
        cidade = cep_info.get('localidade_subordinada')
        if not cidade:
            cidade = cep_info.get('cidade')
        estado = cep_info.get('uf')
        bairro = cep_info.get('bairro')

        idade = pessoas.CalculoIdade(nascimento)
        
        Pessoa = pessoas(CPF,nome,nascimento,idade,email,telefone,cep,estado,cidade,bairro,rua,numeroResidencial)
        
        return Pessoa


    def CalculoIdade(nascimento):
        data_nascimento = datetime.strptime(nascimento, '%Y-%m-%d')
        idade = (datetime.now() - data_nascimento).days // 365.25
        return int(idade)

    def APICPF(CPF, nascimento):
        response = requests.get(f'https://api.infosimples.com/api/v2/consultas/receita-federal/cpf?token=pJ0UhQH3luVjJnzDR_a6XQRr5hoTyeoP4XXXj3R5&timeout=600&ignore_site_receipt=0&cpf={CPF}&birthdate= {nascimento}&origem=web')

        dados_API_CPF = response.json()

        return dados_API_CPF

    def APICEP(cep):
        
        response = requests.get(f'https://api.infosimples.com/api/v2/consultas/correios/cep?token=pJ0UhQH3luVjJnzDR_a6XQRr5hoTyeoP4XXXj3R5&timeout=600&ignore_site_receipt=0&cep={cep}')

        dados_API_CEP = response.json()

        return dados_API_CEP
        


