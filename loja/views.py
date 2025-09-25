from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from loja.models import Produto

def paginaInicialLoja(request):
    return render(request, 'base_loja.html')

# def verProdutoPorSlug(request, produtoSlug):
#     return HttpResponse(f"<h1> Exibindo detalhes do produto: {produtoSlug}</h1>")

def listaProdutosView(request):
    produtosDisponiveis = Produto.objects.filter(estoque__gt = 0)
    contexto = {'produtosDisponiveis': produtosDisponiveis}
    return render(request, 'loja/listaProdutos.html', contexto)
    
def detalheProdutoView(request, produto_id):
    produto = get_object_or_404(Produto, id = produto_id)
    contexto = {'produto': produto}
    return render(request, 'loja/detalheProduto.html', contexto)
    
def sobreLojaView(request):
    return render(request, 'loja/sobre.html')

def contatoLojaView(request):
    return render(request, 'loja/contato.html')

def listaProdutosValiososView(request):
    produtosValiosos = Produto.objects.filter(estoque__gt = 5, preco__gt = 500).order_by("preco")
    contexto = {'produtosValiosos': produtosValiosos}
    return render(request, 'loja/listaProdutosValiosos.html', contexto)

def detalheProdutoValiosoView(request, produto_id):
    produtoValioso = get_object_or_404(Produto, id = produto_id)
    contexto = {'produtoValioso': produtoValioso}
    return render(request, 'loja/detalheProdutoValioso.html', contexto)