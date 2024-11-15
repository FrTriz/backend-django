from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')  # Busca parcial no título
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')  # Busca no nome do autor
    categoria = filters.CharFilter(field_name='categoria__nome', lookup_expr='icontains')  # Busca no nome da categoria

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']
