from django.urls import path
from . import views

urlpatterns = [
    path('bookshelf/', views.list_books, name='list_books'),
    path('bookshelf/create/', views.create_book, name='create_book'),
    path('bookshelf/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('bookshelf/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
