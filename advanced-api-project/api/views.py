"""
View Classes for Book Model:
- BookListView: Lists all books. No authentication required.
- BookDetailView: Retrieves details for a specific book. No authentication required.
- BookCreateView: Creates a new book. Requires authentication.
- BookUpdateView: Updates an existing book. Requires authentication.
- BookDeleteView: Deletes a book. Requires authentication.

Customizations:
- perform_create and perform_update hooks are used to allow custom processing during save.
- Permissions restrict modification actions to authenticated users, while read actions are public.
"""
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwner
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


def index(request):
    return render(request, 'index.html')

# List all books - public access

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


    # DRF filtering, search, and ordering configuration
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed for search
    search_fields = ['title', 'author']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# Retrieve single book by ID - public access
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book - only authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# Update a book - only authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        # Hook for logging or extra validation
        serializer.save()


# Delete a book - only authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
