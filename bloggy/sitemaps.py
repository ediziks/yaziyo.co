from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.conf import settings
from articles.models import Article
from datetime import datetime
from django.utils import dateparse, timezone


class StaticViewSiteMap(Sitemap):
  def items(self):
    return ['home']

  def location(self, item):
    return reverse(item)

  def lastmod(self, item):
    return timezone.now()


class YaziyoSiteMap(Sitemap):
  priority = 0.6

  def items(self):
    return Article.objects.all()

  def lastmod(self, obj):
    return obj.created_date
