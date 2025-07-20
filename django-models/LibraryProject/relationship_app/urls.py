from django.urls import path
from .views import (
    list_books,
    add_book,
    edit_book,
    delete_book,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
    admin_dashboard,
    librarian_dashboard,
    member_dashboard
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/librarian/', librarian_dashboard, name='librarian_dashboard'),
    path('dashboard/member/', member_dashboard, name='member_dashboard'),
]
