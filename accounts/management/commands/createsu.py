
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
  def handle(self, *args, **options):
    if not User.objects.filter(username="zx").exists():
      User.objects.create_superuser("zx", "zx@zx.com", "ediz4845176")
      self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
