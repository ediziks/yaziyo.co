from django.conf import settings


# for pushing Analytics ID key to base.html
def google_analytics(request):
  return {'GA_KEY': settings.GOOGLE_ANALYTICS_KEY}
