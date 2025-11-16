from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


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
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        exclude = ('id',)

    def validate_following(self, value):
        """
        Валидация поля following
        """
        current_user = self.context['request'].user
        if current_user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        if Follow.objects.filter(
            user=current_user,
            following=value
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя!'
            )
        return value
