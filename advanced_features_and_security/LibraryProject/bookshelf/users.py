from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create test users and assign them to groups'

    def handle(self, *args, **kwargs):
        editors_group = Group.objects.get(name='Editors')
        viewers_group = Group.objects.get(name='Viewers')
        admins_group = Group.objects.get(name='Admins')

        User.objects.create_user(username='editor', password='password123', first_name='Editor', last_name='User', email='editor@example.com').groups.add(editors_group)
        User.objects.create_user(username='viewer', password='password123', first_name='Viewer', last_name='User', email='viewer@example.com').groups.add(viewers_group)
        User.objects.create_superuser(username='admin', password='password123', first_name='Admin', last_name='User', email='admin@example.com').groups.add(admins_group)

        self.stdout.write(self.style.SUCCESS('Successfully created test users'))
