from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.contrib import admin
from django.utils import timezone
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO
import os


def image_upload_dir(instance, filename):
  return os.path.join("users/{0}/articles/{1}/".format(instance.user.username, instance.slug), filename)


class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
  title = models.CharField(max_length=255, default='', blank=False)
  message = HTMLField(blank=False, null=False)
  slug = models.SlugField(max_length=140, allow_unicode=True, default='', blank=False, unique=False)
  tags = TaggableManager(blank=True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="article_likes", blank=True)
  created_date = models.DateTimeField(default=timezone.now)
  # published_date = models.DateTimeField()
  image = models.ImageField(default='default_article_image.jpg', upload_to=image_upload_dir, blank=True)
  search_vector = SearchVectorField(null=True, editable=False)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

    if self.image:
      memfile = BytesIO()
      img = Image.open(self.image)

      if img.height > 1920 or img.width > 1080:
        output_size = (1920, 1080)
        img.thumbnail(output_size, Image.BICUBIC)
        if img.mode != 'RGB':
          img = img.convert('RGB')
        img.save(memfile, 'JPEG', optimize=True)
        default_storage.save(self.image.name, memfile)
        memfile.close()
        img.close()

  def all_comments(self):
    return self.comments.all().order_by('-created_date')

  def get_like_url(self):
    return reverse('articles:article-like', kwargs={'username': self.user.username, 'slug': self.slug})

  def __str__(self):
    return 'PK: {} --- TITLE: {}'.format(self.pk, self.title)

  def get_absolute_url(self):
    return reverse('articles:single', kwargs={'username': self.user.username, 'slug': self.slug})

  class Meta:
    indexes = [GinIndex(fields=['search_vector'])]
    ordering = ['-created_date']
    unique_together = ['user', 'slug']


class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField(blank=False)
  created_date = models.DateTimeField(default=timezone.now)
  # approved_comment = models.BooleanField(default=False)

  # def approve(self):
  #   self.approved_comment = True
  #   self.save()

  def __str__(self):
    return 'Comment by {} on {}'.format(self.author, self.article)

  def get_absolute_url(self):
    return reverse('articles:single', kwargs={'pk': self.pk})

  class Meta:
    ordering = ['-created_date']
