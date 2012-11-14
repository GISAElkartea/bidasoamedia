#from __future__ import unicode_literals
import os
from datetime import timedelta


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
    'monkey_team.middleware.MonkeyTeamMiddleware',
    'django_badbrowser.middleware.BrowserSupportDetection',
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
    'preferences.context_processors.preferences_cp',
    'project.context_processors.ajax_template',
    'project.articles.context_processors.category_list',
    'project.feeds.context_processors.feed_list',
    'project.flat.context_processors.flatpage_list',
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

    'south',
    'adminfiles',
    'oembed',
    'markitup',
    'compressor',
    'sorl.thumbnail',
    'djcelery',
    'feedback',
    'preferences',
    'sortable',
    'infinite_pagination',
    'monkey_team',
    'django_badbrowser',

    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    
    'project',
    'project.articles',
    'project.feeds',
    'project.flat',
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


THUMBNAIL_EXTENSION = 'png'
JQUERY_URL = 'js/jquery.min.js'


MARKITUP_FILTER = ('project.utils.markup_filter', {})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'
MARKITUP_AUTO_PREVIEW = True
OEMBED_DEFAULT_PARSE_HTML = False

SASS = os.path.join(os.path.dirname(DIR), 'bin/sass')
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_PRECOMPILERS = (
                ('text/x-sass', '%s {infile} {outfile}' % SASS),
                )

GRAPPELLI_INDEX_DASHBOARD = 'project.dashboard.Dashboard'
GRAPPELLI_ADMIN_TITLE = 'bidasoamedia.info'

# add to WSGI too
import djcelery
djcelery.setup_loader()

BROKER_URL = 'django://'
CELERY_IMPORTS = ('project.feeds.tasks',)
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERYBEAT_SCHEDULE = {
        'update_feeds': {
            'task': 'project.feeds.tasks.update_feeds',
            'schedule': timedelta(seconds=300),
            },
        }

CATEGORY_NUMBER = 5


BADBROWSER_SUGGEST = ('firefox', 'chrome', 'safari', 'opera')
BADBROWSER_REQUIREMENTS = (
    ('firefox', '3.0'),
    ('chrome', '3.0'),
    ('microsoft internet explorer', '8'),
)
