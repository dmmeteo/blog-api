# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django-environ configuration
# https://django-environ.readthedocs.io/en/latest/#how-to-use
import environ
import raven
import psycopg2.extensions

SITE_ROOT = environ.Path(__file__) - 2 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env() # set default values and casting
env.read_env('.env') # reading .env file

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG')
DJANGO_USE_DEBUG_TOOLBAR = env.bool('DJANGO_USE_DEBUG_TOOLBAR')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

ADMINS = tuple([tuple(admins.split(':')) for admins in env.list('DJANGO_ADMINS')])

MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Database configuration
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': env.db('DJANGO_DATABASE_URL'),
}

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'crispy_forms',
)

LOCAL_APPS = (
    'users',
    'base',
    'post',
    'category',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'users.User'
ADMIN_URL = r'^admin/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

#TODO EMAIL CONFIGURATION
EMAIL_BACKEND = env.str('DJANGO_EMAIL_BACKEND')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            SITE_ROOT('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Crispy forms configuration
# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = env.str('DJANGO_STATIC_ROOT')

MEDIA_URL = '/media/'
MEDIA_ROOT = env.str('DJANGO_MEDIA_ROOT')

STATICFILES_DIRS = (
    SITE_ROOT('static'),
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    }
]

# Allauth configuration
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True  # TODO smtp settings

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'base:home'
LOGOUT_REDIRECT_URL = 'account_login'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Sentry configuration
# https://docs.sentry.io/clients/python/integrations/django/
if env('SENTRY_DSN'):
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {
        'dsn': env.str('SENTRY_DSN'),
        'release': raven.fetch_git_sha(SITE_ROOT()),
    }

if DEBUG and DJANGO_USE_DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }
    
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    
    # http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '10.0.2.2')
