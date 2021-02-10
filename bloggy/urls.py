from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage, index, SearchView
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from bloggy.sitemaps import StaticViewSiteMap, YaziyoSiteMap
import notifications.urls


sitemaps = {
    'static': StaticViewSiteMap,
    'yaziyo': YaziyoSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps, 'template_name': 'custom_sitemap.html'}),
    # path('', include('accounts.urls', namespace='accounts')), -> if you don't wanna show accounts prefix in url
    path('articles/', include('articles.urls', namespace='articles')),
    path('search/', SearchView.as_view(), name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'bloggy.views.handler404'
# handler500 = 'bloggy.views.handler500'
# handler403 = 'bloggy.views.my_custom_permission_denied_view'
# handler400 = 'bloggy.views.my_custom_bad_request_view'
