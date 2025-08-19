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
# models.py
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(default=2020)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User,
        related_name='books_created',
        on_delete=models.CASCADE,
        default=1  # Default to user with ID 1
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
# This model includes a foreign key to the Author model
# and a foreign key to the User model to track who created the book record.