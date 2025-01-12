from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_venda, name='cadastrar_venda'),
    path('listar/', views.listar_vendas, name='listar_vendas'),
    path('', views.VendaListView.as_view(), name='vendas'),  # Aqui chamamos a VendaListView
]
