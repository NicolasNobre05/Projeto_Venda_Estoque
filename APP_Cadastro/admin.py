from django.contrib import admin

from .models import *

admin.site.register(Cliente)

admin.site.register(Funcionario)

admin.site.register(Fornecedor)

admin.site.register(Lojas)

admin.site.register(Produtos)