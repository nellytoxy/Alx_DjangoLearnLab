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

# Blog Post Management

## Overview
This Django blog project includes CRUD functionalities for managing blog posts.

## Features
- **Create:** Authenticated users can create new blog posts.
- **Read:** All users can view a list of posts and details of individual posts.
- **Update:** Authors can edit their own posts.
- **Delete:** Authors can delete their own posts.

## URL Patterns
- **Post List:** `/` - List all blog posts.
- **Post Detail:** `/post/<id>/` - View details of a specific post.
- **Post Create:** `/post/new/` - Create a new post.
- **Post Edit:** `/post/<id>/edit/` - Edit an existing post.
- **Post Delete:** `/post/<id>/delete/` - Delete an existing post.

## Testing
1. **Create Post:** Navigate to `/post/new/` to create a post.
2. **Read Post:** Navigate to `/` to view posts and `/post/<id>/` for details.
3. **Update Post:** Navigate to `/post/<id>/edit/` to edit a post.
4. **Delete Post:** Navigate to `/post/<id>/delete/` to delete a post.

## Permissions
- **Create:** Only authenticated users can create posts.
- **Update/Delete:** Only the author of the post can edit or delete it.
