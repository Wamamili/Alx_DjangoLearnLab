from rest_framework import serializers
from .models import Book
# api/serializers 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
