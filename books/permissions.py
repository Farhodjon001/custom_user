from rest_framework.permissions import BasePermission

class BookCreatePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.roles==1