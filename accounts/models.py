from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from articles.models import Article
from django.contrib import admin
from PIL import Image


def get_username(request):
  username = None
  if request.user.is_authenticated():
    username = request.user.username


class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
  # email = models.EmailField(max_length=150, unique=True, blank=False, null=False)
  bio = models.TextField(max_length=280, blank=True)
  avatar = models.ImageField(default='default_avatar.jpg', upload_to='avatars/')
  cover = models.ImageField(default='default_cover.jpg', upload_to='covers/')
  followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='is_following', blank=True)
  bookmarks = models.ManyToManyField(Article, related_name='is_bookmark', blank=True)
  # TBD
  # activated = models.BooleanField(default=False)

  def __str__(self):
    return '@{}'.format(self.user.username)

  def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.avatar.url)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size, Image.BICUBIC)
      img.save(self.avatar.url, optimize=True)

    img2 = Image.open(self.cover.path)
    if img2.height > 1920 or img2.width > 1080:
      img2_output_size = (1920, 1080)
      img2.thumbnail(img2_output_size, Image.BICUBIC)
      img2.save(self.cover.path, optimize=True)


# Profile and User objects sync
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  # Creates user profile after signup
  if created:
    Profile.objects.create(user=instance)
  instance.profile.save()
