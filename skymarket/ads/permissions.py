from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не создавали этого объявления!'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
