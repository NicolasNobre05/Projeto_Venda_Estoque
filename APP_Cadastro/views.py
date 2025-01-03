import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from django.shortcuts import render
from utils.tratamento_dados import data_menor
from .utils import APICEP
import requests
from datetime import datetime
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def CadastroFornecedor(request):
    if request.method == 'POST':
        fornecedor_info = empresa.Cadastro(request)
        if fornecedor_info == False:
            return render(request, 'CadastroFornecedor.html')
        novo_fornecedor = Fornecedor()
        novo_fornecedor.cnpj =  fornecedor_info.CNPJ
        novo_fornecedor.nome = fornecedor_info.nome
        novo_fornecedor.email = fornecedor_info.email
        novo_fornecedor.telefone = fornecedor_info.telefone
        novo_fornecedor.cep = fornecedor_info.cep
        novo_fornecedor.estado = fornecedor_info.estado
        novo_fornecedor.cidade = fornecedor_info.cidade
        novo_fornecedor.bairro = fornecedor_info.bairro
        novo_fornecedor.rua = fornecedor_info.rua
        novo_fornecedor.numeroResidencial = fornecedor_info.numeroResidencial
        novo_fornecedor.save()
    return render(request, 'CadastroFornecedor.html')

def CadastroLoja(request):
    if request.method == 'POST':
        loja_info = empresa.Cadastro(request)
        if loja_info == False:
            return render(request, 'CadastroLoja.html')
        novo_loja = Lojas()
        novo_loja.cnpj =  loja_info.CNPJ
        novo_loja.nome = loja_info.nome
        novo_loja.email = loja_info.email
        novo_loja.telefone = loja_info.telefone
        novo_loja.cep = loja_info.cep
        novo_loja.estado = loja_info.estado
        novo_loja.cidade = loja_info.cidade
        novo_loja.bairro = loja_info.bairro
        novo_loja.rua = loja_info.rua
        novo_loja.numeroResidencial = loja_info.numeroResidencial
        novo_loja.save()
    return render(request, 'CadastroLoja.html')

def CadastroProduto(request):
    if request.method == 'POST':
        produto_info = produtos.Cadastro(request)
        if produto_info == False:
            return render(request, 'CadastroProduto.html')
        novo_produto = Produtos()
        novo_produto.descricao =  produto_info.descricao
        novo_produto.preco = produto_info.preco
        novo_produto.unidadeMedida = produto_info.unidadeMedida
        novo_produto.save()
    return render(request, 'CadastroProduto.html')

def CadastroCliente(request):
    if request.method == 'POST':
        #INFORMAÇÕES DO CLIENTE
        Cliente_info = pessoas.Cadastro(request)
        if Cliente_info == False:
            return render(request, 'cliente.html')
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
        if funcionario_info == False:
            return render(request, 'CadastroVendedor.html')
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
        if dados_API_CPF['data'] == []:
            messages.error(request, 'CPF inválido')
            return False
            
        pessoa_info = dados_API_CPF['data'][0]
        nome = pessoa_info.get('nome')
        ano_obito = pessoa_info.get('ano_obito')
        
        if ano_obito is not None:
            messages.error(request, 'CPF inválido')
            return False
        
        #PEGER NOME DA CIDADE/ESTADO E BAIRRO

        cep_info_pessoa = APICEP(cep) 
        cidade = cep_info_pessoa.get('cidade')
        estado = cep_info_pessoa.get('estado')
        bairro = cep_info_pessoa.get('bairro')

        idade = pessoas.CalculoIdade(nascimento)
        
        Pessoa = pessoas(CPF,nome,nascimento,idade,email,telefone,cep,estado,cidade,bairro,rua,numeroResidencial)
        
        return Pessoa
        
    def CalculoIdade(nascimento):
        data_nascimento = datetime.strptime(nascimento, '%Y-%m-%d')
        idade = (datetime.now() - data_nascimento).days // 365.25
        return int(idade)

    def APICPF(CPF, nascimento):
        response = requests.get(f'https://api.infosimples.com/api/v2/consultas/receita-federal/cpf?token=pJ0UhQH3luVjJnzDR_a6XQRr5hoTyeoP4XXXj3R5&timeout=600&ignore_site_receipt=0&cpf={CPF}&birthdate= {nascimento}&origem=web')

        if response.status_code != 200:
            raise Exception(f'Erro ao consultar a API: {response.status_code}')

        dados_API_CPF = response.json()

        return dados_API_CPF

class empresa:
    def __init__(self, CNPJ, nome,email,telefone,cep,estado,cidade,bairro,rua,numeroResidencial):
        self.CNPJ = CNPJ
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numeroResidencial = numeroResidencial


    def Cadastro(request):
        CNPJ = request.POST.get('cnpj')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numeroResidencial = request.POST.get('numeroResidencial')

        cep_info_empresa = APICEP(cep) 
        cidade = cep_info_empresa.get('cidade')
        estado = cep_info_empresa.get('estado')
        bairro = cep_info_empresa.get('bairro')

        Empresa = empresa(CNPJ,nome,email,telefone,cep,estado,cidade,bairro,rua,numeroResidencial)

        return Empresa

class produtos:
    def __init__(self, descricao, preco, unidadeMedida):
        self.descricao = descricao
        self.preco = preco
        self.unidadeMedida = unidadeMedida
    
    def Cadastro(request):
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        unidadeMedida = request.POST.get('unidadeMedida')
        if not descricao or not preco or not unidadeMedida:
            return False
            
        print(descricao,preco,unidadeMedida)
        novo_produto = produtos(descricao,preco,unidadeMedida)
        return novo_produto
    
    