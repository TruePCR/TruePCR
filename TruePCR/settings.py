"""
Django settings for TruePCR project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ux$tg!x3vmhf&autsr-3t1n*xz!h1ipacozha%i4+l+i))6^rt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TruePCR.apps.datasets',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'TruePCR.urls'

WSGI_APPLICATION = 'TruePCR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'DATABASE_URL' in os.environ: # production environment
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    TEMPLATE_DEBUG = True
    S3_BACKEND = True
    # DB config
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    # allow all host headers
    ALLOWED_HOSTS = ['*']
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else: # development environment
    DEBUG = True
    TEMPLATE_DEBUG = True
    S3_BACKEND = False
    # print e-mails to the console instead of sending them
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, '../static') # for the base Yeoman template
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
    os.path.join(BASE_DIR, '../.tmp') # during grunt serve
)

# S3 file storage backend
if S3_BACKEND:
    #DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
    # for boto:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    # TODO: rethink input type=submit
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    #from storages.backends.s3 import CallingFormat
    #AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# logging

import logging

LOG_PATH, LOG_FILENAME = '.', 'TruePCR.log'
LOG_LEVEL = logging.DEBUG
LOG_MAX = 10**6 # bytes

logging.basicConfig(
    level=LOG_LEVEL,
    handlers=[logging.StreamHandler()]
    # format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] %(message)s',
    # handlers=[
    #     logging.handlers.RotatingFileHandler(
    #         os.path.join(LOG_PATH, LOG_FILENAME), maxBytes=LOG_MAX
    #     ), # file output
    #     logging.StreamHandler() # stdout
    # ]
)
