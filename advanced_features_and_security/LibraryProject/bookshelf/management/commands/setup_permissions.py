from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from models import Book

class Command(BaseCommand):
    help = 'Sets up user groups and permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Define permissions
        view_permission = Permission.objects.get(codename='can_view_mymodel')
        create_permission = Permission.objects.get(codename='can_create_mymodel')
        edit_permission = Permission.objects.get(codename='can_edit_mymodel')
        delete_permission = Permission.objects.get(codename='can_delete_mymodel')

        # Assign permissions to groups
        editors_group.permissions.add(create_permission, edit_permission)
        viewers_group.permissions.add(view_permission)
        admins_group.permissions.add(view_permission, create_permission, edit_permission, delete_permission)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
