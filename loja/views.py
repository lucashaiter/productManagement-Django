from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from loja.models import Produto

def paginaInicialLoja(request):
    return render(request, 'base_loja.html')

def verProdutoPorSlug(request, produtoSlug):
    return HttpResponse(f"<h1> Exibindo detalhes do produto: {produtoSlug}</h1>")

def listaProdutosView(request):
    produtosDisponiveis = Produto.objects.filter(estoque__gt = 0) 
    contexto = {'produtos': produtosDisponiveis}
    return render(request, 'loja/listaProdutos.html', contexto)
    
def detalheProdutoView(request, produto_id):
    produto = get_object_or_404(Produto, id = produto_id)
    contexto = {'produto': produto}
    return render(request, 'loja/detalheProduto.html', contexto)
    