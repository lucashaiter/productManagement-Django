from django.urls import path
from .views import views, ProdutoListView, ProdutoDetailView

appName = "loja"

urlpatterns = [
    path('sobre/', views.sobreLojaView, name="sobre"),
    path('contato/', views.contatoLojaView, name="contato"),
    
    path('lista-produtos/', views.listaProdutosView, name="lista_produtos"),
    path('lista-produtos/produto/<int:produto_id>/', views.detalheProdutoView, name="detalhe_produto"),

    path('lista-produtos-valiosos/', views.listaProdutosValiososView, name="lista_produtos_valiosos"),
    path('lista-produtos-valiosos/produtoValioso/<int:produto_id>/', views.detalheProdutoValiosoView, name="detalhe_produto_valioso"),
    
    path('lista-produtos-produtos/', ProdutoListView.as_view() ,name="lista_produtos_produtos"),
    path('lista-produtos-produto/produtoProduto/<int:pk>/', ProdutoDetailView.as_view(), name="detalhe_produto_produto"),
]
