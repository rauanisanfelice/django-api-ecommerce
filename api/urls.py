from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ProdutoList, ProdutoDetail, CategoriaList, CategoriaDetail, \
    UserList, UserDetail


urlpatterns = [
    # Produtos
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='produto-detail'),

    # Categorias
    path('categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),

    # User
    path('users/', UserList.as_view(), name='usuario-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='usuario-detail'),
    
]