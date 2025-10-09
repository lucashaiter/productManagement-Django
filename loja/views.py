from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Produto, Cliente
from django.views.generic import ListView, DetailView

# Defs
def paginaInicialLoja(request):
    return render(request, 'baseLoja.html')

# -------------------------------------------------------------------------

def listaProdutosView(request):
    produtosDisponiveis = Produto.objects.filter(estoque__gt = 0)
    contexto = {'produtosDisponiveis': produtosDisponiveis}
    return render(request, 'loja/listaProdutos.html', contexto)
    
def detalheProdutoView(request, produto_id):
    produto = get_object_or_404(Produto, id = produto_id)
    contexto = {'produto': produto}
    return render(request, 'loja/detalheProduto.html', contexto)

# -------------------------------------------------------------------------
    
def sobreLojaView(request):
    return render(request, 'loja/sobre.html')

# -------------------------------------------------------------------------

def contatoLojaView(request):
    return render(request, 'loja/contato.html')

# -------------------------------------------------------------------------

def listaProdutosValiososView(request):
    produtosValiosos = Produto.objects.filter(estoque__gt = 5, preco__gt = 500).order_by("preco")
    contexto = {'produtosValiosos': produtosValiosos}
    return render(request, 'loja/listaProdutosValiosos.html', contexto)

def detalheProdutoValiosoView(request, produto_id):
    produtoValioso = get_object_or_404(Produto, id = produto_id)
    contexto = {'produtoValioso': produtoValioso}
    return render(request, 'loja/detalheProdutoValioso.html', contexto)

# -------------------------------------------------------------------------

def listaClientesView(request):
    clientes = Cliente.objects.all()
    contexto = {'clientesLista': clientes}
    return render(request, 'loja/listaClientes.html', contexto)

# -------------------------------------------------------------------------
def produtoListFBV(request):
    produtosEstoque = Produto.objects.filter(estoque__gt = 0).order_by('nome')
    contexto = {
        'produtos': produtosEstoque,
        'tituloPagina': 'Nossos produtos disponíveis'
    }
    
    return render(request, 'loja/listaProdutosProdutos.html', contexto)

# --------------------------------------------------------------------------

# Classes
class ProdutoListView(ListView):
    model = Produto
    template_name = 'loja/listaProdutosProdutos.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.filter(estoque__gt = 0).order_by('nome')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'loja/detalheProdutoProduto.html'
    context_object_name = 'produto'
    