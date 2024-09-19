from django.urls import path
from .views import RegisterView, CustomAuthToken

print("Loading accounts.urls")


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]
