from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ProdutoList, ProdutoDetail, CategoriaList, CategoriaDetail

urlpatterns = [
    # Produtos
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='produto-detail'),

    # Categorias
    path('categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
]