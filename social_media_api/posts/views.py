from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from .serializers import PostSerializer  # Ensure you import your PostSerializer

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # Create or get a Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:  # If the Like was created, generate a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type= ContentType.objects.get_for_model(Post),
                target_object_id=post.id,
            )
            return Response({"message": "Post liked."}, status=201)

        return Response({"message": "Already liked."}, status=400)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"message": "Post unliked."}, status=204)
