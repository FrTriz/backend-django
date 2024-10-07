# biblioteca/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from biblioteca.models import Categoria, Autor, Livro  # Importando os modelos

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        # Criação de categorias
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_romance = Categoria.objects.create(nome="Romance")

        # Criação de autores
        autor_agatha_christie = Autor.objects.create(nome="Agatha Christie")
        autor_arthur_c_clarke = Autor.objects.create(nome="Arthur C. Clarke")
        autor_arthur_conan_doyle = Autor.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(nome="Emily Brontë")
        autor_george_rr_martin = Autor.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(nome="Isaac Asimov")
        autor_jrr_tolkien = Autor.objects.create(nome="J.R.R. Tolkien")

        # Criação de livros
        Livro.objects.create(
            titulo="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1934-01-01",
        )
        Livro.objects.create(
            titulo="Morte no Nilo",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1937-11-01",
        )
        Livro.objects.create(
            titulo="2001: Uma Odisseia no Espaço",
            autor=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1968-06-16",
        )
        Livro.objects.create(
            titulo="As Crônicas de Nárnia",
            autor=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        # Continue criando livros conforme necessário...
