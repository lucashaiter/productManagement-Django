from django.urls import path
from . import views

appName = "loja"

urlpatterns = [
    # path('', views.paginaInicialLoja, name="loja"),
    # path('produto/<slug:produtoSlug>/', views.verProdutoPorSlug, name="ver_produtos"), 
    path('lista-produtos/', views.listaProdutosView, name="lista_produtos"),
    path('produto/<int:produto_id>/', views.detalheProdutoView, name="detalhe_produto"),
    path('', views.paginaInicialLoja, name="loja"),
]