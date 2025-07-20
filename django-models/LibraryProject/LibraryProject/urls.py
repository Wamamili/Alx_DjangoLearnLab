from django.contrib import admin
from django.urls import path, include
from relationship_app import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_books, name='home'),  # Root URL shows book list
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
