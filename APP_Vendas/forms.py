# forms.py
from django import forms
from .models import Venda
from APP_Cadastro.models import Produtos, Cliente, Funcionario, Lojas

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['loja','cliente', 'vendedor', 'produtos', 'valor_total', 'forma_pagamento', 'codigo_venda']
        
    loja = forms.ModelChoiceField(queryset=Lojas.objects.all())
    produtos = forms.ModelMultipleChoiceField(queryset=Produtos.objects.all(), widget=forms.CheckboxSelectMultiple)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())  
    vendedor = forms.ModelChoiceField(queryset=Funcionario.objects.all())  