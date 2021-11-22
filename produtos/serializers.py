from rest_framework import serializers
from .models import Fornecedor, Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',
            'descricao',
            'quantidade',
            'data_validade',
            'ativo',
            'fornecedor',
        )

    def validate_quantidade(self, valor):
        if valor <= 100:
            return valor
        raise serializers.ValidationError("A quantidade não pode ser maior que 100 unidades.")

class FornecedorSerializer(serializers.ModelSerializer):

    # produtos = ProdutoSerializer(many=True, read_only=True)

    """produtos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='produto-detail'
    )"""

    produtos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    quantidade_produtos = serializers.SerializerMethodField()

    class Meta:
        extra_kargs = {
            'email': {'write_only': True}
        }
        model = Fornecedor
        fields = (
            'id',
            'descricao',
            'telefone',
            'produtos',
            'quantidade_produtos'
        )

    def get_quantidade_produtos(self, obj):
        produtos = Produto.objects.filter(fornecedor=obj.id)
        return len(produtos)