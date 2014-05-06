#coding: utf-8

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wavzkd&v3$0p4y%m36cz(!1ga4l1u+j#1um8us(jc++mw(l!)j'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    's3_folder_storage',
    'planeta_brasil.api_copa',
    'planeta_brasil.aguia_verde',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'planeta_brasil.urls'

WSGI_APPLICATION = 'planeta_brasil.wsgi.application'


#DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), }}

import dj_database_url
DATABASES['default'] =  dj_database_url.config()


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     '/var/www/static/',
# )

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)


#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#AWS_S3_SECURE_URLS = False       # use http instead of https
#AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
#DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'

DEFAULT_S3_PATH = 'media'
STATIC_S3_PATH = 'static'

AWS_S3_ACCESS_KEY_ID = 'AKIAIPX66T6O2QZJ5ECQ'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'planetabrasil'

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'