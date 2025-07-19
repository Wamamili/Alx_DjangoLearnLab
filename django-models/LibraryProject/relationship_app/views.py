# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ This line includes both models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Or use select_related('author') for performance
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
