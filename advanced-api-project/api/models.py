# models.py
# This file contains the models for the Author and Book entities.
from django.db import models
from datetime import datetime

# Author model stores basic author information
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

# Book model stores details of books written by authors
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # related_name='books' allows reverse lookup: author.books.all()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
# Review model stores reviews for books