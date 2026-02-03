from rest_framework import permissions

class CanCreateShortURL(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user and request.user.has_perm('shortener.add_urlshortener')
        return True