# blog/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]

# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('/<int:pk>/update/', post_detail, name='post_detail'), 
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('/<int:pk>/update/', post_detail, name='post_detail'),   
]