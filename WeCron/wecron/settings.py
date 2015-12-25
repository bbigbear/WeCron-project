"""
Django settings for wecron project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if 'DJ_SECRET_KEY' not in os.environ:
    print 'WARNING: need to set DJ_SECRET_KEY in the environment'
    os.environ['DJ_SECRET_KEY'] = 'wb7dh*#f!x1y_=0d8$i_rgafhy9gpv9jf3^=jasewr^vmmd7)n'
SECRET_KEY = os.environ['DJ_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DJ_DEBUG' not in os.environ

ALLOWED_HOSTS = ['.weixin.at']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wxhook',
    'remind'
)

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

ROOT_URLCONF = 'wecron.urls'

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

WSGI_APPLICATION = 'wecron.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('WECRON_DB_HOST', 'localhost'),
        'PORT': os.environ.get('WECRON_DB_PORT', 5432),
        'NAME': os.environ.get('WECRON_DB_NAME', 'wecron'),
        'USER': os.environ.get('WECRON_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('WECRON_DB_PASSWORD', ''),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'wxhook.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s - %(name)s - [%(asctime)s] %(message)s , %(thread)d - %(threadName)s : %(process)d - %(processName)s',
            'datefmt': '%d/%b %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}

WX_APPID = os.environ.get('WX_APPID', 'xxx')
WX_APPSECRET = os.environ.get('WX_APPSECRET', 'xxx')
WX_SIGN_TOKEN = os.environ.get('WX_SIGN_TOKEN', 'xxx')

