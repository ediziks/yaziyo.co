"""bloggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage, index, SearchView
import notifications.urls
# from filebrowser.sites import site


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/filebrowser/', site.urls),
    path('', index, name='home'),
    # path('', include('accounts.urls', namespace='accounts')), -> if you don't wanna show accounts prefix in url
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('search/', SearchView.as_view(), name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'bloggy.views.my_custom_page_not_found_view'
# handler500 = 'bloggy.views.my_custom_error_view'
# handler403 = 'bloggy.views.my_custom_permission_denied_view'
# handler400 = 'bloggy.views.my_custom_bad_request_view'