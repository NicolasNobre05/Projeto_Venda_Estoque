from django.shortcuts import render, redirect
from APP_Vendas.forms import VendaForm  
from APP_Vendas.models import Venda
from django.views.generic import ListView

def cadastrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('venda_sucesso')  
    else:
        form = VendaForm()  

    return render(request, 'cadastrar_venda.html', {'form': form})

def listar_vendas(request):
    vendas = Venda.objects.all()  
    return render(request, 'listar_vendas.html', {'vendas': vendas})

class VendaListView(ListView):
    model = Venda
    template_name = 'listar_vendas.html'  
    context_object_name = 'vendas' 