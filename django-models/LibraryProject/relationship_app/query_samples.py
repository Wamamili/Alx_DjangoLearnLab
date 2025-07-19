# relationship_app/query_samples.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author = Author.objects.get(name="Chinua Achebe")
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a library using variable
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # 3. Retrieve the librarian for the library
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian of {library.name}: {librarian.name}")

if __name__ == '__main__':
    run_queries()
