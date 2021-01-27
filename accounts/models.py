from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from articles.models import Article
from django.contrib import admin
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO
import os


def get_username(request):
  username = None
  if request.user.is_authenticated():
    username = request.user.username


def cover_upload_dir(instance, filename):
  return os.path.join("users/{}/covers".format(instance.user.username), filename)


def avatar_upload_dir(instance, filename):
  return os.path.join("users/{}/avatars".format(instance.user.username), filename)


class Profile(models.Model):

  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
  # email = models.EmailField(max_length=150, unique=True, blank=False, null=False)
  bio = models.TextField(max_length=280, blank=True)
  avatar = models.ImageField(default='default_avatar.jpg', upload_to=avatar_upload_dir)
  # cover = models.ImageField(default='default_cover.jpg', upload_to='covers/')
  cover = models.ImageField(default='default_cover.jpg', upload_to=cover_upload_dir)
  followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='is_following', blank=True)
  bookmarks = models.ManyToManyField(Article, related_name='is_bookmark', blank=True)
  # TBD for email authentication
  # activated = models.BooleanField(default=False)

  def __str__(self):
    return '@{}'.format(self.user.username)

  def save(self, *args, **kwargs):
    # run save of parent class above to save original image to disk
    super().save(*args, **kwargs)

    if self.avatar:
      memfile = BytesIO()

      try:
        img = Image.open(self.avatar)
        if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size, Image.BICUBIC)
          if img.mode != 'RGB':
            img = img.convert("RGB")
          img.save(memfile, 'JPEG', optimize=True)
          default_storage.save(self.avatar.name, memfile)
          memfile.close()
          img.close()
        else:
          img.thumbnail(img.size, Image.BICUBIC)
          if img.mode != 'RGB':
            img = img.convert('RGB')
          img.save(memfile, 'JPEG', optimize=True)
          default_storage.save(self.image.name, memfile)
          memfile.close()
          img.close()
      # images not found exc
      except (FileNotFoundError, AttributeError):
        pass

    if self.cover:
      memfile = BytesIO()

      try:
        img = Image.open(self.cover)
        if img.height > 1920 or img.width > 1080:
          output_size = (1920, 1080)
          img.thumbnail(output_size, Image.BICUBIC)
          if img.mode != 'RGB':
            img = img.convert("RGB")
          img.save(memfile, 'JPEG', optimize=True)
          default_storage.save(self.cover.name, memfile)
          memfile.close()
          img.close()
        else:
          img.thumbnail(img.size, Image.BICUBIC)
          if img.mode != 'RGB':
            img = img.convert('RGB')
          img.save(memfile, 'JPEG', optimize=True)
          default_storage.save(self.image.name, memfile)
          memfile.close()
          img.close()
      except FileNotFoundError:
        pass


# Profile and User objects sync
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  # Creates user profile after signup
  if created:
    Profile.objects.create(user=instance)
  instance.profile.save()
