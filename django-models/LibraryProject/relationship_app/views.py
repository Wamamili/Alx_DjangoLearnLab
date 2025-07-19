# relationship_app/views.py
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    # Option 1: With select_related (better performance if accessing author info)
    books = Book.objects.select_related('author').all()

    # Option 2: Basic version using Book.objects.all()
    # books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
