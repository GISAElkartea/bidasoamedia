# -*- coding: utf-8 -*-
from settings import *

try:
    from secret_key import SECRET_KEY
except ImportError:
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)
    with open(os.path.join(DIR, 'secret_key.py'), 'w') as secret_key_file:
        secret_key_file.write("SECRET_KEY = '{}'".format(SECRET_KEY))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False


STATIC_ROOT = '/home/bidasoamedia/webapps/static/static/'
STATIC_URL = '/files/static/'
MEDIA_ROOT = '/home/bidasoamedia/webapps/static/media/'
MEDIA_URL = '/files/media/'
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'grappelli')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/bidasoamedia/webapps/bidasoamedia/memcached.sock',
        'TIMEOUT': 60,
    }
}

CACHE_MIDDLEWARE_SECONDS = 90
MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',
                    'django.middleware.gzip.GZipMiddleware') +\
                    MIDDLEWARE_CLASSES + \
                    ('django.middleware.http.ConditionalGetMiddleware',
                    'django.middleware.cache.FetchFromCacheMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                    )

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
        }


ADMINS = (('Unai Zalakain', '{}@{}'.format('contact', 'unaizalakain.info')),)
MANAGERS = ADMINS

FEEDBACK_EMAIL = ''
EMAIL_SUBJECT_PREFIX = '[BM]'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'system@bidasoamedia.info'
SERVER_EMAIL = 'system@bidasoamedia.info'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
