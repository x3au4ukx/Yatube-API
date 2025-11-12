from django.shortcuts import get_object_or_404
from rest_framework import (
    filters, mixins, pagination, permissions, response, status, viewsets
)

from posts.models import Follow, Group, Post, User
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для операций с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        """Автоматически назначает автора при создании поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet только для чтения данных о группах."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для операций с комментариями к постам."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        """Возвращает комментарии конкретного поста."""
        return self._get_post().comments.all()

    def perform_create(self, serializer):
        """Создает комментарий для конкретного поста."""
        serializer.save(
            author=self.request.user,
            post=self._get_post()
        )

    def _get_post(self):
        """Возвращает пост по ID из URL параметров."""
        return get_object_or_404(Post, id=self.kwargs.get('post_pk'))


class FollowViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """ViewSet для операций с подписками."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Возвращает только подписки текущего пользователя."""
        return self.request.user.follows.all()

    def perform_create(self, serializer):
        """Автоматически назначает пользователя отправившего запрос."""
        serializer.save(user=self.request.user)
