from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "marca", "estoque")
    search_fields = ("nome", "marca", "descricao")
    list_filter = ("marca",)
