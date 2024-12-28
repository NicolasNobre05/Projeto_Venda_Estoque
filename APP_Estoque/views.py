from django.shortcuts import render

# Create your views here.

def RequisicaoCompra(request):
    return render(request, 'RequisicaoCompra.html')

def Pedido(request):
    return render(request, 'Pedido.html')

