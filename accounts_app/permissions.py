from rest_framework.permissions import IsAdminUser


class IsSuperUser(IsAdminUser):  # Проверка на SuperUser
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)