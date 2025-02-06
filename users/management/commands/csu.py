from django.core.management import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    """Команда для создания суперадмина"""
    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email="admin@sky.ru",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("123")
        user.save()