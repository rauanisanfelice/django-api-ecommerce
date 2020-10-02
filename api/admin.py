from django.contrib import admin
from .models import Produto, Categoria


@admin.register(Produto)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class AuthorAdmin(admin.ModelAdmin):
    pass