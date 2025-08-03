from rest_framework.generics import ListAPIView
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
