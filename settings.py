# Django settings for bluehillsports_com project.

DEBUG = True
TESTING=False
TEMPLATE_DEBUG = DEBUG

import os.path
PROJECT_DIR = os.path.dirname(__file__)

ADMINS = (
    ('Colin Powell', 'colin@onecardinal.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.sqlite3.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
if DEBUG:
    if TESTING:
        DATABASE_ENGINE='mysql'
        DATABASE_NAME = 'bhsports'
        DATABASE_USER = 'root'
        DATABASE_PASSWORD = 'mainr0ot'
        MEDIA_URL = 'http://bhsports.rubyvroom.com/'
    else:
        DATABASE_ENGINE = 'sqlite3'
        DATABASE_NAME = 'dev.db'
        MEDIA_URL = 'http://localhost:8000/m/'
        GOOGLE_API_KEY="ABQIAAAATux_aKmAEX7DnojAr8SqlRT2yXp_ZAY8_ufC3CFXhHIE1NvwkxQyeuUWRNQot2nGx4DfX_1xGXt7cA"
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
else:
    DATABASE_ENGINE='mysql'
    DATABASE_NAME = 'bhsports'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'mainr0ot'
    MEDIA_ROOT='/home/powellc/public_html/bluehillsports.com/public/media'
    MEDIA_URL = 'http://static.bluehillsports.com'
        
ADMIN_MEDIA_PREFIX=MEDIA_URL+'admin/'
LOGIN_REDIRECT_URL = '/'
SECRET_KEY = '(4vs_n(5(u&6a9*3p0k6izx6inb-d&xx8#wf7v7#*+&i)v#=in'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INTERNAL_IPS=('localhost',)
ROOT_URLCONF = 'bluehillsports_com.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'tagging',
    'typogrify',
    'schedule',
    'athletics',
)
