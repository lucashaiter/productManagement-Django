from django import forms
from.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        # 1. Diz ao ModelForm qual model ele deve usar.
        model = Produto
        # 2. Lista os campos do model que devem aparecer no formulário.
        fields = ['nome', 'descricao', 'preco', 'categoria', 'estoque', 'image']