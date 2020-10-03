from django.db import models


class Categoria(models.Model):
    
    nome            = models.CharField(max_length=50)
    descricao       = models.CharField(max_length=100, null=True, verbose_name='Descrição')
    ativo           = models.BooleanField(default=True)
    data_inclusao   = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Data de inclusão")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Produto(models.Model):

    nome                = models.CharField(max_length=50)
    descricao           = models.CharField(max_length=100, verbose_name='Descrição')
    preco               = models.FloatField(verbose_name='Preço')
    qtde_disponivel     = models.IntegerField(verbose_name='Quantidade disponível')

    ativo           = models.BooleanField(default=True)
    data_inclusao   = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Data de inclusão")
    data_alteracao  = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, verbose_name="Data de alteração")
    data_exclusao   = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, verbose_name="Data de exclusão")

    user_inclusao   = models.CharField(max_length=50, verbose_name="Usuário inclusão")
    user_alteracao  = models.CharField(max_length=50, verbose_name="Usuário alteração")
    user_exclusao   = models.CharField(max_length=50, verbose_name="Usuário exclusão")

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome