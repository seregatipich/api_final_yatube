from django.contrib.auth import get_user_model
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post, Group, Follow, User
from api.serializers import PostSerializer, \
    GroupSerializer, CommentSerializer, FollowSerializer
from api.permissions import AuthorOrReading


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorOrReading)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_field = ('group')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorOrReading)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
