from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from relationship_app.views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    path('admin-area/', admin_view.admin_dashboard, name='admin_view'),
    path('librarian-area/', librarian_view.librarian_dashboard, name='librarian_view'),
    path('member-area/', views.member_dashboard, name='member_view'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library'),

    # Book management URLs
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Role-based views
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('member_dashboard/', views.member_dashboard, name='member_dashboard'),
]

