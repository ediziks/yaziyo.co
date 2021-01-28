"""
Django settings for bloggy project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import environ
from django.conf import settings
# for aws logging
from boto3.session import Session


env = environ.Env(DEBUG=(bool, True))
# Reads .env
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ['USER'] == 'zx':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'bloggy-dev.eu-central-1.elasticbeanstalk.com', 'yaziyo.co', '*.yaziyo.co', 'www.yaziyo.co']

# ADMIN_ENABLED = False # or DEBUG

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    # added later but needed?
    'django.contrib.postgres',
    # apps
    'articles',
    'accounts',
    'bloggy',
    # 3rd
    'bootstrap4',
    'widget_tweaks',
    'django_social_share',
    'taggit',
    'el_pagination',
    'captcha',
    'notifications',
    'storages',
    'tinymce',
    'easy_thumbnails',
]


if os.environ['USER'] != 'zx':
    DEBUG_PROPAGATE_EXCEPTIONS = True
    # AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'yaziyo-staticfilesandmedia'
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_S3_FILE_OVERWRITE = True
    # AWS_DEFAULT_ACL = None
    AWS_DEFAULT_ACL = 'public-read'
    STATIC_URL = '/static/'  # for eb to serve
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')  # for eb to serve
    # statics below are to serve from s3
    # STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic/static/')  # for eb to serve
    # STATIC_LOCATION = 'static'
    # STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATIC_LOCATION)
    # STATICFILES_STORAGE = 'bloggy.custom_storage.StaticStorage'
    AWS_PRELOAD_METADATA = True     # Speeds up the load of the filebrowser files
    AWS_QUERYSTRING_AUTH = False    # Speeds up the load of the filebrowser files
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
    DEFAULT_FILE_STORAGE = 'bloggy.custom_storage.MediaStorage'
    THUMBNAIL_DEFAULT_STORAGE = 'bloggy.custom_storage.ThumbnailStorage'
    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'formatters': {
    #         'verbose': {
    #             'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
    #                        'pathname=%(pathname)s lineno=%(lineno)s ' +
    #                        'funcname=%(funcName)s %(message)s'),
    #             'datefmt': '%Y-%m-%d %H:%M:%S'
    #         },
    #         'simple': {
    #             'format': '%(levelname)s %(message)s'
    #         }
    #     },
    #     'handlers': {
    #         'null': {
    #             'level': 'DEBUG',
    #             'class': 'logging.NullHandler',
    #         },
    #         'console': {
    #             'level': 'DEBUG',
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'verbose'
    #         }
    #     },
    #     'loggers': {
    #         'testlogger': {
    #             'handlers': ['console'],
    #             'level': 'INFO',
    #         }
    #     }
    # }
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic/static/')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'allstatic/staticfiles/'),)
    MEDIA_ROOT = os.path.join(BASE_DIR, 'allstatic/media/')
    MEDIA_URL = '/media/'


# allauth signup infos
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'twitter': {

    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bloggy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  # For EL-pagination
                'bloggy.context_processors.google_analytics',  # For Google Analytics Key to base.html
            ],
        },
    },
]

WSGI_APPLICATION = 'bloggy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('NAME'),
            'USER': env('USER'),
            'PASSWORD': env('PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'tr-TR'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 2

RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')

if not DEBUG:
    GOOGLE_ANALYTICS_KEY = env('GOOGLE_ANALYTICS_KEY')
else:
    GOOGLE_ANALYTICS_KEY = 'notonlocaldev'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_REQUIRED = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 80
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

TAGGIT_CASE_INSENSITIVE = True

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SECURE_REFERRER_POLICY = 'same-origin'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


TINYMCE_COMPRESSOR = False
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tinymce")
TINYMCE_EXTRA_MEDIA = {
    'js': [
        STATIC_URL + "tinymce/tinymce.min.js",
        STATIC_URL + "js/tinycustom.js"
    ]
}
# TINYMCE_JS_URL = "/static/tinymce/tinymce.min.js"
# TINYMCE_JS_ROOT = "/static/tinymce"

# TINYMCE_DEFAULT_CONFIG = {
#     # 'plugins': "image, imagetools,table,spellchecker,wordcount",
#     'selector': 'textarea',
#     # 'mode': 'textareas',
#     # 'selector': 'textarea',
#     'theme': "silver",
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 10,
#     'min_height': 500,
#     # 'toolbar': [
#     #     'undo redo | bold italic underline | fontselect fontsizeselect',
#     #     'forecolor backcolor | alignleft aligncenter alignright alignfull | numlist bullist outdent indent'
#     # ],
#     # 'skin': {'content': 'dark', 'ui': 'oxide-dark'}
#     # 'inline': True,
#     'plugins': ['quickbars', 'wordcount', 'preview', 'codesample', 'imagetools', 'hr', 'link', 'spellchecker', 'lists', 'media', 'fullscreen', 'autoresize'],
#     'toolbar': ['undo redo | fullscreen'],
#     'menubar': False,
#     # 'statusbar': False,
#     'quickbars_insert_toolbar': ' media quickimage pageembed | bullist numlist | hr',
#     'quickbars_selection_toolbar': 'bold italic underline blockquote | h1 h2 codesample | link | alignleft aligncenter alignright alignjustify | preview',
#     'quickbars_image_toolbar': 'alignleft aligncenter alignright | blockquote | '
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True


# TINYMCE_DEFAULT_CONFIG = {
#     'height': 300,
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'silver',
#     'plugins': 'textcolor save link image media preview codesample contextmenu table code lists fullscreen  insertdatetime  nonbreaking contextmenu directionality searchreplace wordcount visualblocks visualchars code fullscreen autolink lists  charmap print  hr anchor pagebreak',
#     'toolbar1': '''
#             fullscreen preview bold italic underline | fontselect,
#             fontsizeselect  | forecolor backcolor | alignleft alignright |
#             aligncenter alignjustify | indent outdent | bullist numlist table |
#             | link image media | codesample |
#             ''',
#     'toolbar2': '''
#             visualblocks visualchars |
#             charmap hr pagebreak nonbreaking anchor |  code |
#             ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
# }
