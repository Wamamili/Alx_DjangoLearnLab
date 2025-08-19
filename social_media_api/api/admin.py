from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
# This file registers the Author and Book models with the Django admin site.
# This allows these models to be managed through the Django admin interface.