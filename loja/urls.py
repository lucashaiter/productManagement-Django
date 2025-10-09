from django.urls import path
from . import views
from .views import ProdutoListView, ProdutoDetailView

appName = "loja"

urlpatterns = [
    path('', views.paginaInicialLoja, name="inicio"),
    
    path('sobre/', views.sobreLojaView, name="sobre"),
    path('contato/', views.contatoLojaView, name="contato"),
    
    path('lista-produtos/', views.listaProdutosView, name="lista_produtos"),
    path('lista-produtos/produto/<int:produto_id>/', views.detalheProdutoView, name="detalhe_produto"),

    path('lista-produtos-valiosos/', views.listaProdutosValiososView, name="lista_produtos_valiosos"),
    path('lista-produtos-valiosos/produtoValioso/<int:produto_id>/', views.detalheProdutoValiosoView, name="detalhe_produto_valioso"),
    
    # FBV - def
    path('lista-produtos-produtos-fbv/', views.produtoListFBV, name="produto_list_fbv"),
    
    # CBV - Class
    path('lista-produtos-produtos/', ProdutoListView.as_view() ,name="lista_produtos_produtos"),
    path('lista-produtos-produto/produtoProduto/<int:pk>/', ProdutoDetailView.as_view(), name="detalhe_produto_produto"),
    
    path('clientes/', views.listaClientesView, name="lista_clientes")
]
