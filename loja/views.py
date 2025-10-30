from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Produto, Cliente
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import ProdutoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    
    
# --------------------------------------------------------------------------

# Create View
class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'loja/produtoForm.html'
    success_url = reverse_lazy('lista_produtos_produtos')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    

# Update View
class ProdutoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'loja/produtoForm.html'
    success_url = reverse_lazy('lista_produtos_produtos')
    
    def test_func(self):
        produto = self.get_object()
        return self.request.user == produto.usuario

# Delete View
class ProdutoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Produto
    template_name = 'loja/produtoDelete.html'  # Para confirmação da deleção
    success_url = reverse_lazy('lista_produtos_produtos')
    
    def test_func(self):
        produto = self.get_object()
        return self.request.user == produto.usuario
    
# --------------------------------------------------------------------------

class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'