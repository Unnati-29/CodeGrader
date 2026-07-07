from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from accounts.models import Profile

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser(
                username='admin',
                password='Admin@1234',
                email='admin@codegrader.com'
            )
            Profile.objects.get_or_create(user=user, defaults={'role': 'teacher'})
            self.stdout.write('Superuser created: admin / Admin@1234')
        else:
            self.stdout.write('Superuser already exists')