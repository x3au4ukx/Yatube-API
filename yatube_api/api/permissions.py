from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsAuthenticatedAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """Разрешает чтение всем, изменение только авторизованному автору."""

    def has_object_permission(self, request, view, content):
        return request.method in SAFE_METHODS or content.author == request.user
