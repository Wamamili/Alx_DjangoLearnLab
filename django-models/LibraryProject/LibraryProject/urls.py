
from django.contrib import admin
from django.urls import path, include
from relationship_app import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include app routes
]
