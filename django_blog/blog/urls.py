from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # URL pattern for viewing the details of a specific post
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    
    # URL pattern for creating a new comment on a specific post
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    
    # URL pattern for updating a specific comment
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    
    # URL pattern for deleting a specific comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
