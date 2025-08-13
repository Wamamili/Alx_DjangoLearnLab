# blog/urls.py

from django.urls import path
from . import views
from .views import (
    BlogLoginView,
    BlogLogoutView,
    register,
    profile,
    profile_edit,
    
)

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),
]
