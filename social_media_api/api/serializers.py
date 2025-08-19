# serializers.py
# This file contains serializers for the Author and Book models.
from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

# Serializes all fields of the Book model with validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id', 'created_by']


    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializes Author with nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested representation of related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']