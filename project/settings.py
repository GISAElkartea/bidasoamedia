#from __future__ import unicode_literals
import os

_ = lambda x: x
DIR = os.path.dirname(__file__)


SITE_ID = 1


USE_I18N = True
USE_L10N = True
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'eu'
LANGUAGES = (
        ('eu', 'Euskara'),
        )
LOCALE_PATHS = ( os.path.join(DIR, 'locale'), )


MEDIA_ROOT = os.path.join(DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(DIR, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/grappelli/'
STATICFILES_DIRS = [os.path.join(DIR, 'assets')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

TEMPLATE_LOADERS = (
    'yammy.django_loaders.YammyFileSystemLoader',
    'yammy.django_loaders.YammyPackageLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    os.path.join(DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.comments',

    'adminfiles',
    'oembed',
    'markitup',
    'compressor',
    
    'project',
    'project.articles',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

X_FRAME_OPTIONS = 'DENY'

THUMBNAIL_EXTENSION = 'png'
JQUERY_URL = 'js/jquery.min.js'


ADMINFILES_YOUTUBE_USER = ''
ADMINFILES_VIMEO_USER = ''
ADMINFILES_FLICKR_USER = ''
ADMINFILES_FLICKR_API_KEY = ''


#MARKITUP_FILTER = ('project.utils.markup_filter', {'safe_mode': True})
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

SASS = os.path.join(os.path.dirname(DIR), 'bin/sass')
COMPRESS_PRECOMPILERS = (
                ('text/x-sass', '%s {infile} {outfile}' % SASS),
                )
