from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read for anyone, write only for owner
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Posts from people the user follows + their own posts
        following_ids = user.followers.values_list("id", flat=True)
        return Post.objects.filter(author__id__in=following_ids).order_by("-created_at")
    
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        # Get all users the current user follows
        following_users = request.user.following.all()

        # Query posts from those users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


