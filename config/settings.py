import os
from datetime import timedelta, datetime
from pathlib import Path

import pytz
from dotenv import load_dotenv

NULLABLE = {"null": True, "blank": True}

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-$=s1^jq53q=1f#=y(3-0c50nmqgqx%8_lb=nu%cf-hrme-)0d@'
DEBUG = True

load_dotenv(BASE_DIR / '.env')
SERVICE_ADDR = os.getenv('SERVICE_ADDR') if os.getenv('SERVICE_ADDR') is not None else 'http://127.0.0.1:8000'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'django_rename_app',
    'django_filters',
    'django_celery_beat',
    'drf_yasg',

    'authen_drf',
    'lms',
    'payment',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
    ]
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

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

LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = "Asia/Yakutsk"

USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authen_drf.User'
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

# СТАТИЧЕСКИЕ ФАЙЛЫ
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# МЕДИА ФАЙЛЫ
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

MODERATORS_GROUP_NAME = 'moderator'
USERS_GROUP_NAME = 'user'

# ПОЧТА
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# CELERY
CELERY_BROKER_URL = os.getenv("CELERY_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_URL")
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULE = {
    'check_user_activities': {
        'task': 'lms.tasks.check_user_activities',
        'schedule': timedelta(seconds = 10),
        'start_time': datetime.now(pytz.timezone(TIME_ZONE))
    },
}


