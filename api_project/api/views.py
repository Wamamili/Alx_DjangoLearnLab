# api/views.py
from numpy import generic
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(generic.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# api/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

