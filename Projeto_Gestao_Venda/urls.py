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
from django.urls import path
from APP_Cadastro.views import CadastroFornecedor,CadastroLoja ,CadastroProduto, CadastroCliente, CadastroVendedor
from APP_Estoque.views import RequisicaoCompra,Pedido
from APP_Vendas.views import Vendas

urlpatterns = [
    path('cadastrofornecedor/', CadastroFornecedor, name='cadastrofornecedor'),
    path('cadastroloja/', CadastroLoja, name='cadastroloja'),
    path('cadastroproduto/', CadastroProduto, name='cadastroproduto'),
    path('cadastrocliente/', CadastroCliente, name='cadastrocliente'),
    path('cadastrovendedor/', CadastroVendedor, name='cadastrovendedor'),
    path('requisicaocompra/', RequisicaoCompra, name='requisicaocompra'),
    path('pedido/', Pedido, name='pedido'),
    path('vendas/', Vendas, name='vendas'),
    path('admin/', admin.site.urls),
]
