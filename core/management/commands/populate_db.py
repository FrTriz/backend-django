from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        # Criar Categorias
        categorias = [
            "Mistério", "Ficção", "Fantasia", "Romance"
        ]
        categorias_obj = {nome: Categoria.objects.create(nome=nome) for nome in categorias}

        # Criar Autores
        autores = [
            "Agatha Christie", "Arthur C. Clarke", "Arthur Conan Doyle",
            "C.S. Lewis", "Emily Brontë", "George R.R. Martin",
            "Isaac Asimov", "J.R.R. Tolkien"
        ]
        autores_obj = {nome: Autor.objects.create(nome=nome) for nome in autores}

        # Criar Livros
        livros = [
            ("Assassinato no Expresso do Oriente", "Agatha Christie", "Mistério", "1934-01-01"),
            ("Morte no Nilo", "Agatha Christie", "Mistério", "1937-11-01"),
            ("2001: Uma Odisseia no Espaço", "Arthur C. Clarke", "Ficção", "1968-06-16"),
            ("Encontro com Rama", "Arthur C. Clarke", "Ficção", "1973-06-01"),
            ("O Cão dos Baskervilles", "Arthur Conan Doyle", "Mistério", "1902-04-01"),
            ("Um Estudo em Vermelho", "Arthur Conan Doyle", "Mistério", "1887-11-01"),
            ("As Crônicas de Nárnia", "C.S. Lewis", "Fantasia", "1950-10-16"),
            ("O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", "Fantasia", "1950-10-16"),
            ("O Morro dos Ventos Uivantes", "Emily Brontë", "Romance", "1847-12-01"),
            ("A Guerra dos Tronos", "George R.R. Martin", "Fantasia", "1996-08-06"),
            ("Fundação", "Isaac Asimov", "Ficção", "1951-06-01"),
            ("O Hobbit", "J.R.R. Tolkien", "Fantasia", "1937-09-21"),
        ]

        for titulo, autor, categoria, publicado_em in livros:
            Livro.objects.create(
                titulo=titulo,
                autor=autores_obj[autor],
                categoria=categorias_obj[categoria],
                publicado_em=publicado_em
            )

