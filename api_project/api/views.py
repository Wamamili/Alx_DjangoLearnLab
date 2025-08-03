from rest_framework.permissions import IsAuthenticated # Import permission class for authentication
from rest_framework.generics import ListAPIView # Import generic view for listing
from rest_framework import generics, viewsets # Import viewsets for CRUD operations
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book

# ViewSet for Book model to handle CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# List view for Book model
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
