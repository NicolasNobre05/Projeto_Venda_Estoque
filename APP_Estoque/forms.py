from django import forms
from .models import RequisicaoCompra

class RequisicaoCompraForm(forms.ModelForm):
    class Meta:
        model = RequisicaoCompra
        fields = '__all__'  
