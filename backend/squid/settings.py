"""
Django settings for squid project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Generated Nov 20th 18:27
SECRET_KEY = 'lx$yin4fnpme%4e(svbb^j0k9imq$3%%7rv%cc38dn(@76n=s('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This is a security flaw, use CORS_ALLOWED_ORIGINS in production
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'user.apps.UserConfig',
    'application.apps.ApplicationConfig',
    'insurance.apps.InsuranceConfig',
    'payment.apps.PaymentConfig',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',

]

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # baba
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'squid.urls'

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
            ],
        },
    },
]

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'squid.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'template1',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5430',
#         'TEST': {
#             'MIRROR': 'default',
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ftxybkan',
        'USER': 'ftxybkan',
        'PASSWORD': 'u9__2EYiyjn4qWHrpjT8QQsMrSPu31u4',
        'HOST': 'balarama.db.elephantsql.com',
        'PORT': '5432',
        'TEST': {
            'MIRROR': 'default',
        }
    }
}
# postgres://ftxybkan:u9__2EYiyjn4qWHrpjT8QQsMrSPu31u4@balarama.db.elephantsql.com/ftxybkan



ALLOWED_HOSTS = [
    "savegame-env.eba-fijpimur.eu-west-2.elasticbeanstalk.com",
    "localhost:3000",
    "localhost",
    "127.0.0.1",
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        ('rest_framework.permissions.IsAuthenticated',)
    ),
    'DATETIME_FORMAT': '%s000',
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# FOR TESTING
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '3d5774375bfad8'
# EMAIL_HOST_PASSWORD = 'b3a3cc06188638'
# EMAIL_PORT = '2525'

# TODO: make the keys hidden in proudction... but this is the info for prod

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'AKIAYDHX7T7YQBWU37GD'
AWS_SECRET_ACCESS_KEY = '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'

# EMAIL_HOST = 'email-smtp.eu-west-2.amazonaws.com'
# EMAIL_HOST_USER = 'AKIAYDHX7T7YXQSINV46'  # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = 'BEcu173yLq/L50J9itIgBIXAeZbkgvFx6ynwdDotc26T'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'savegame@gmail.com'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=200000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
