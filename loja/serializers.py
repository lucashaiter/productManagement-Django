from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome'
        ]

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.StringRelatedField(source="categoria", read_only=True)
    usuario_nome = serializers.StringRelatedField(source="usuario", read_only=True)
    
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'categoria_nome',
            'categoria',
            'estoque',
            'image',
            'usuario_nome',
            'usuario'
        ],
        
        extra_kwargs = [
            'categoria': ['write_only': True],
            'usuario': ['write_only': True],
        ]