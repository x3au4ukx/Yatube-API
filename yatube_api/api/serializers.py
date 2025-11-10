from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


class BaseAuthorSerializer(serializers.ModelSerializer):
    """Базовый сериализатор с полем author."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(BaseAuthorSerializer):
    """Сериализатор для модели Post."""

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(BaseAuthorSerializer):
    """Сериализатор для модели Comment."""

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'author')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Follow
        exclude = ('id',)
