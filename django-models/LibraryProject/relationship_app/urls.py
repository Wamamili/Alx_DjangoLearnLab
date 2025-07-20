from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from relationship_app.views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    path('admin-area/', admin_view.admin_dashboard, name='admin_view'),
    path('librarian-area/', librarian_view.librarian_dashboard, name='librarian_view'),
    path('member-area/', views.member_dashboard, name='member_view'),
    path('register/', views.register_view, name='register'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
