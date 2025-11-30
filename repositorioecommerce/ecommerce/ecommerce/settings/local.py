from .base import *

SECRET_KEY = 'django-insecure-u8kz=^36%+p**-##k2m$2s@u%o&!xlld$%9+rd8)a(fx(spl9s'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}