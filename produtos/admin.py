from django.contrib import admin
from .models import Fornecedor, Produto


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id','descricao', 'email', 'telefone', 'criacao', 'ativo')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'quantidade', 'data_validade', 'ativo', 'fornecedor', 'criacao')
