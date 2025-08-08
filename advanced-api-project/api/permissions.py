# permissions.py
# This file contains custom permissions for the Book model.
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only the creator of the book to update or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
