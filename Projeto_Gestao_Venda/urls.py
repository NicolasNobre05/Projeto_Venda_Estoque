"""
URL configuration for Projeto_Gestao_Venda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from APP_Cadastro.views import CadastroFornecedor, CadastroLoja, CadastroProduto, CadastroCliente, CadastroVendedor, home 
from APP_Estoque.views import cadastrar_requisicao, listar_pedidos
from APP_Vendas.views import cadastrar_venda
from APP_Vendas.views import Venda
from APP_Estoque import views

urlpatterns = [
    path('cadastrofornecedor/', CadastroFornecedor, name='cadastrofornecedor'),
    path('cadastroloja/', CadastroLoja, name='cadastroloja'),
    path('cadastroproduto/', CadastroProduto, name='cadastroproduto'),
    path('cadastrocliente/', CadastroCliente, name='cadastrocliente'),
    path('cadastrovendedor/', CadastroVendedor, name='cadastrovendedor'),
    path('requisicaocompra/', cadastrar_requisicao, name='requisicaocompra'),  # Use a view correta aqui
    path('pedido/', listar_pedidos, name='pedido'),  # Use uma view para listar ou gerenciar pedidos
    path('vendas/', include('APP_Vendas.urls')),
    path('listar_requisicoes/', views.ListarRequisicoesView.as_view(), name='listar_requisicoes'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
