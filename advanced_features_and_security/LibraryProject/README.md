=# Custom Permissions and Groups Setup

## Permissions

- `can_view_mymodel`: Allows viewing of `MyModel` instances.
- `can_create_mymodel`: Allows creation of `MyModel` instances.
- `can_edit_mymodel`: Allows editing of `MyModel` instances.
- `can_delete_mymodel`: Allows deletion of `MyModel` instances.

## Groups

- **Editors**: Can create and edit `MyModel` instances.
- **Viewers**: Can view `MyModel` instances.
- **Admins**: Can view, create, edit, and delete `MyModel` instances.

## Setup

1. Run `python manage.py setup_permissions` to create and assign permissions.
2. Run `python manage.py create_test_users` to create test users and assign them to groups.
3. Test the permissions by logging in with test users and verifying access levels.
