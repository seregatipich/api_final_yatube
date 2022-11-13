from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import SlugRelatedField
from posts.models import Post, Group, Comment, Follow, User

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    post = serializers.SlugRelatedField(
        read_only=True, slug_field='id')

    def validate(self, data):
        if not data:
            raise serializers.ValidationError(
                'Коментарий не должен быть пустым'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Comment
        validators = []


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate_following(self, value):
        user = self.context.get('request').user
        if user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value

    class Meta:
        model = Follow
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            ),
        )
