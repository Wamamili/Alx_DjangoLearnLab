from rest_framework import serializers
from .models import Book
# api/serializers.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
