from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Optional list-only view
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),  # Token endpoint
    path('', include(router.urls)),  # Automatically handles CRUD routes
]
