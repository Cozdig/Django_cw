from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создает группу Manager с правами просмотра"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Manager")

        if created:
            permissions = [
                ("view_mailings", "mailing", "mailings"),
                ("view_recipient", "mailing", "recipient"),
                ("view_message", "mailing", "message"),
            ]

            for codename, app_label, model in permissions:
                try:
                    perm = Permission.objects.get(
                        codename=codename,
                        content_type__app_label=app_label,
                        content_type__model=model,
                    )
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    pass

            self.stdout.write("Группа создана")
        else:
            self.stdout.write("Группа уже существует")
