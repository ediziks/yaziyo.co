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
import django_heroku
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
# DEBUG = env('DEBUG')
DEBUG = True

ALLOWED_HOSTS = ['demo-bloggy.herokuapp.com/', '127.0.0.1', 'localhost', 'bloggy-dev.eu-central-1.elasticbeanstalk.com', '172.31.7.73', '172.31.32.97', '18.194.190.186', '172.31.45.194', 'yaziyo.co', '.yaziyo.co']


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
]


if 'AWS_ACCESS_KEY_ID' in os.environ:
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
    # AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    STATIC_LOCATION = 'static'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATIC_LOCATION)
    STATICFILES_STORAGE = 'bloggy.custom_storage.StaticStorage'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # FILEBROWSER_DEFAULT_PERMISSIONS = None
    # FILEBROWSER_LIST_PER_PAGE = 5  # Speeds up the load of the filebrowser files
    # AWS_PRELOAD_METADATA = True     # Speeds up the load of the filebrowser files
    # AWS_QUERYSTRING_AUTH = False    # Speeds up the load of the filebrowser files
    # MEDIA_LOCATION = 'media'
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
    # DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", MEDIA_URL)
    DEFAULT_FILE_STORAGE = 'bloggy.custom_storage.MediaStorage'
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
    # STATICFILES_DIRS = (
    #     '/var/app/curent/staticfiles',
    # )
    STATICFILES_DIRS = (
        '/home/zx/Desktop/bloggy/staticfiles',
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


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


# FILEBROWSER SETTINGS
# DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'media/uploads/')
# IMAGE_MAXBLOCK = getattr(settings, 'FILEBROWSER_IMAGE_MAXBLOCK', 1024 * 1024)
# MAX_UPLOAD_SIZE = getattr(settings, "FILEBROWSER_MAX_UPLOAD_SIZE", 10485760)
# VERSION_QUALITY = getattr(settings, 'FILEBROWSER_VERSION_QUALITY', 90)


SITE_ID = 1

RECAPTCHA_PUBLIC_KEY = '6LfYfd8ZAAAAAGhY9dkqugc76CflIP-kTW4abiqv'
RECAPTCHA_PRIVATE_KEY = '6LfYfd8ZAAAAAOtXHBsBmK8jbAhIwQ4hWIGL38g5'

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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# if not DEBUG:
#     SECURE_HSTS_SECONDS = 31536000
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     SECURE_SSL_REDIRECT = False
#     SECURE_REFERRER_POLICY = 'same-origin'
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     # Activate Django - Heroku.
#     django_heroku.settings(locals())


TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tinymce")
# TINYMCE_FILEBROWSER = True
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


# TINYMCE_JS_URL = "/static/tinymce/tinymce.min.js"
# TINYMCE_JS_ROOT = "/static/tinymce"

TINYMCE_EXTRA_MEDIA = {
    'js': [
        STATIC_URL + "tinymce/tinymce.min.js",
        STATIC_URL + "js/tinycustom.js"
    ]
}
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
#     'toolbar': ['fullscreen undo redo '],
#     # 'menubar': False,
#     # 'statusbar': False,
#     'quickbars_insert_toolbar': ' media quickimage pageembed | bullist numlist | hr',
#     'quickbars_selection_toolbar': 'bold italic underline blockquote | h1 h2 codesample | link | alignleft aligncenter alignright alignjustify | preview',
#     'quickbars_image_toolbar': 'alignleft aligncenter alignright | blockquote | '
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True
# TINYMCE_EXTRA_MEDIA = {
#     'css': {
#         'all': [
#             ...
#         ],
#     },
#     'js': [
#         ...
#     ],
# }


# CKEditor
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor"
# CKEDITOR_UPLOAD_PATH = "/media/articles/images/"
# CKEDITOR_RESTRICT_BY_USER = True
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_IMAGE_MAX_WIDTH = '100'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono-lisa',
#         # 'skin': 'office2013',
#         'toolbar': 'Basic',
#         'toolbar_CustomToolbar': [
#             # {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             # {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             # {'name': 'forms',
#             #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#             #            'HiddenField']},
#             # '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'Image', 'Table', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['BulletedList', 'NumberedList', '-', 'Blockquote', 'CodeSnippet', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
#             {'name': 'links', 'items': ['Link', 'Unlink']},
#             # {'name': 'insert',
#             #  'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             # '/',
#             {'name': 'styles', 'items': ['Font', 'Format']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'Preview', ]},
#             # put this to force next toolbar on new line
#         ],
#         'toolbar': 'CustomToolbar',  # put selected toolbar config here
#         'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document', 'doctools']}],
#         'height': 'auto',
#         'width': 'auto',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 900,
#         'toolbarCanCollapse': False,
#         'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 2,
#         # image size
#         # 'imageResize': {
#         #     'maxWidth': 800,
#         #     'maxHeight': 800,
#         # },
#         'extraPlugins': ','.join([
#             # 'uploadimage',  # the upload image feature
#             # your extra plugins here
#             # 'div',
#             'autolink',
#             # 'autoembed',
#             # 'autocomplete',
#             # 'image2',
#             # 'easyimage',
#             # 'imagebase',
#             'codesnippet',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             # 'emoji',
#             'button',
#             'panelbutton',
#             'clipboard',
#             # 'textmatch',
#             # 'textwatcher',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }
