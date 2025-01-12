from django.shortcuts import render, redirect
from .models import RequisicaoCompra
from .forms import RequisicaoCompraForm
from .models import Pedido
from django.views.generic import ListView

# Cadastro de Requisição de Compra
def cadastrar_requisicao(request):
    if request.method == 'POST':
        form = RequisicaoCompraForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('sucesso') 
    else:
        form = RequisicaoCompraForm()  
    return render(request, 'RequisicaoCompra.html', {'form': form})

# Listar todas as requisições de compra
class ListarRequisicoesView(ListView):
    model = RequisicaoCompra
    template_name = 'listar_requisicoes.html' 
    context_object_name = 'requisicoes' 

def listar_pedidos(request):
    pedidos = Pedido.objects.all() 
    return render(request, 'template_name.html', {'pedidos': pedidos})
