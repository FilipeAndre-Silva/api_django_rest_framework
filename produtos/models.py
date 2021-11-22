from django.core.validators import MinValueValidator
from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fornecedor(Base):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['id']

    def __str__(self):
        return self.descricao


class Produto(Base):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)], null=False, blank=False)
    data_validade = models.DateTimeField(null=False, blank=False)
    ativo = models.BooleanField(default=False)
    fornecedor = models.ForeignKey(Fornecedor, related_name='produtos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao
