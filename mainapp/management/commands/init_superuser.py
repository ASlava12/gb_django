from django.core.management.base import BaseCommand

from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser(
            input("Введите логин администратора: "),
            input("Введите email администратора: "),
            input("Введите пароль: "),
            age=int(input("Введите возраст: ")),
        )
