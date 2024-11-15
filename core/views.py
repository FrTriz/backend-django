from rest_framework import generics
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .filters import LivroFilter


# View para recuperar, atualizar e deletar livros
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"



class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ['^titulo', '^autor__nome', '^categoria__nome']  # Busca pelo início do termo
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']  # Ordenação permitida


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['^nome']  # Busca pelo início do nome do autor
    ordering_fields = ['nome']  # Permite ordenação por nome


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ['^nome']  # Busca pelo início do nome da categoria
    ordering_fields = ['nome']  # Permite ordenação por nome
