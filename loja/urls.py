from django.urls import path
from . import views

appName = "loja"

urlpatterns = [
    # path('', views.paginaInicialLoja, name="loja"),
    # path('produto/<slug:produtoSlug>/', views.verProdutoPorSlug, name="ver_produtos"), 
    path('lista-produtos/', views.listaProdutosView, name="lista_produtos"),
    path('lista-produtos/produto/<int:produto_id>/', views.detalheProdutoView, name="detalhe_produto"),
    path('sobre/', views.sobreLojaView, name="sobre"),
    path('contato/', views.contatoLojaView, name="contato"),
    path('lista-produtos-valiosos/', views.listaProdutosValiososView, name="lista_produtos_valiosos"),
    path('lista-produtos-valiosos/produtoValioso/<int:produto_id>/', views.detalheProdutoValiosoView, name="detalhe_produto_valioso")
]