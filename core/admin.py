from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'resenha', 'lido', 'criado_em', 'modificado_em')
