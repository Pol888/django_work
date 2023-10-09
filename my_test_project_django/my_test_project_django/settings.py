"""
Django settings for my_test_project_django project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import logging
from pathlib import Path
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# 'django-insecure-$nt3#i!cir3m$@omoor003r_wekcr-^0d3(-^9(g*gr#*6tg0j'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '192.168.1.136',
    '127.0.0.1',
    'supersite.pythonanywhere.com'
]


# Application definition

INSTALLED_APPS = [
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'my_test_app',
    #'my_test_app_2',
    #my_test_app_3',
    'my_test_app_4',
    'my_test_app_5',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'my_test_project_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'my_test_project_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supersite$default',
        'USER': 'supersite',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'supersite.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',

        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = BASE_DIR / 'static/'
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#"formatters": {
#        "verbose": {
#            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
#            "style": "{",
#        },
#        "simple": {
#            "format": "{levelname} {message} ",
#            "style": "{",
#        },
#    },
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',
#            "formatter": "simple",
#        },
#        'file': {
#            'class': 'logging.FileHandler',
#            'filename': './dj.log',
#            "formatter": "verbose",
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console', 'file'],
#            'level': 'INFO',
#        },
#        'my_test_app_2': {
#            'handlers': ['console', 'file'],
#            'level': 'INFO'
#        },
#        'my_test_app': {
#            'handlers': ['console', 'file'],
#            'level': 'INFO'
#        }
#    },
#}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

INTERNAL_IPS = ['127.0.0.1']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


