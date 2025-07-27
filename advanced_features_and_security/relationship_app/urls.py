from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Dashboards
    path('admin_view/', views.admin_dashboard, name='admin_view'),
    path('librarian_view/', views.librarian_dashboard, name='librarian_view'),
    path('member_view/', views.member_dashboard, name='member_view'),

    # User Management
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Book CRUD
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    path('', lambda request: redirect('list_books'))
]
