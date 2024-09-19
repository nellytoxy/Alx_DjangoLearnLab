from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    # Override groups and user_permissions fields to prevent clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )
