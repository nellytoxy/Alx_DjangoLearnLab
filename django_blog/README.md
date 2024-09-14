# Django Blog Authentication System

## Overview
This project includes user authentication features for registration, login, logout, and profile management.

## Setup
1. Ensure `django.contrib.auth` and `django.contrib.contenttypes` are included in `INSTALLED_APPS`.
2. Add URL patterns to `urls.py`.
3. Create HTML templates in `templates/registration`.

## Testing
- **Registration:** Go to `/register/` to create a new account.
- **Login:** Go to `/login/` to log in.
- **Profile:** Go to `/profile/` to view and edit your profile.
- **Logout:** Go to `/logout/` to log out.

## Security
- **CSRF Protection:** Ensure `{% csrf_token %}` is included in forms.
- **Password Security:** Handled by Django’s built-in hashing.
