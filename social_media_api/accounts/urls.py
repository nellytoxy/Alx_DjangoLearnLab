from django.urls import path
from .views import RegisterView, CustomAuthToken
from .views import FollowUserView, UnfollowUserView

print("Loading accounts.urls")


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),

]
