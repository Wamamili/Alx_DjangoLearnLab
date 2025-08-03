from rest_framework.authtoken.views import obtain_auth_token # Import the token authentication view
from django.contrib import admin
from django.urls import path, include # Include the necessary Django URL functions

# api_project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    # Other API endpoints can be included here
]
