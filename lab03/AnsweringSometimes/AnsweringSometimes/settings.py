"""
Django settings for AnsweringSometimes project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from os import getenv
import os
import getpass
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rc=_rqt(znst^x+k+cq8x+t3$56-0%^h76^ambt7e-0wnqg@59'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', 
    'ascapp'
]


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'search_backend.apps.SearchBackendConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AnsweringSometimes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AnsweringSometimes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

def get_secret(secret_name):
    with open(f"/run/secrets/{secret_name}") as f:
        return f.read().rstrip()

if getenv("DEPLOYED") == "1":
    db_name = get_secret('db_name')
    db_user = get_secret('db_usr')
    db_password = get_secret('db_pwd')
    db_host = 'postgres'
else:
    db_name = 'asc_db'
    db_user = input('DB username: ')
    db_password = getpass.getpass('DB password: ')
    db_host = '127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom auth user model
AUTH_USER_MODEL = "account.User"

# aws s3
if getenv('USE_S3') == '1':
    secrets_path = os.path.join(os.path.dirname(__file__), 'secrets.txt')
    secrets = None
    with open(secrets_path) as f:
        secrets = json.loads(f.read())

    AWS_S3_ACCESS_KEY_ID = secrets['AWS_S3_ACCESS_KEY_ID']
    AWS_S3_SECRET_ACCESS_KEY = secrets['AWS_S3_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'ilya0.0mazin0.0bucket'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_REGION_NAME = 'ru-central1'
    AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
    AWS_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
# media
    MEDIA_ROOT = BASE_DIR / 'local_storage/'
    MEDIA_URL = 'local_storage/'
