"""
Django settings for mozzi_django project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from mongoengine import connect
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['a304.site', '127.0.0.1', 'localhost']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g)2howhcux-dfu^m@934()fjvvd%vezh=(-19oyhc7#&t5sb5h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CELERY_BROKER_URL = 'redis://localhost:6379/0'
TIME_ZONE = 'Asia/Seoul'

# Application definition

INSTALLED_APPS = [
    'datas',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mozzi_django.urls'

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

WSGI_APPLICATION = 'mozzi_django.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


### 로컬용
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mozzi',
#         'USER': 'ssafy',
#         'PASSWORD': 'ssafy',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     },
#     'mongodb': {
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': False,
#         'NAME': 'my_mongodb_database',
#         'HOST': 'localhost',  # 여기서는 호스트 이름만 지정합니다.
#         'PORT': '27017',  # 포트는 정수로 지정합니다.
#     }
# }
# connect(
#     db='my_mongodb_database',  # 여기에는 사용할 MongoDB 데이터베이스 이름을 넣으세요.
#     host='mongodb://localhost:27017/',  # MongoDB 호스트 주소입니다. 포트 번호 27017을 사용합니다.
#     alias='default',  # 이 부분은 Django에서 사용할 alias를 설정하는 부분입니다.
# )
### 서버용
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mozzi',
        'USER': 'ssafy',
        'PASSWORD': 'ssafy',
        'HOST': 'a304.site',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': 'mozzi',       
        
        'CLIENT' : {
            'host': 'a304.site',  # 여기서는 호스트 이름만 지정합니다.
            'port': 27017,  # 포트는 정수로 지정합니다.
            'username': 'root',
            'password': 'ssafy',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }


}

connect(
    db='mozzi',
    host='a304.site',
    port=27017,
    username='root',
    password='ssafy',
    authentication_source='admin',
    authentication_mechanism='SCRAM-SHA-1'
)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://a304.site:6379/1',  # 여기서 '1'은 레디스 데이터베이스 번호입니다.
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
CELERY_BROKER_URL = 'redis://a304.iste:6379/0'
CELERY_RESULT_BACKEND = 'redis://a304.iste:6379/0'

CELERY_BEAT_SCHEDULE = {
    'reset_food_today_views': {
        'task': 'your_app.tasks.reset_food_views',
        'schedule': crontab(hour=0, minute=0),  # 매일 오전 12시 실행
    },
}
# 추가로, 세션, 캐시 및 기타 사용 사례에 레디스를 사용하려면 다음과 같이 설정할 수 있습니다.
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
