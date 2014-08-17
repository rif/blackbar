import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
    'ENGINE':  'django.db.backends.sqlite3',
       'NAME': 'blackbar.db',
    }
}
TIME_ZONE = 'Europe/Bucharest'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/upload')
#MEDIA_URL =  '/static/upload/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tvt$_gdda8(m!$k5^v46wmj67s-!0+c&9edx&)8rb5m3&_)sy('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'blackbar.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blackbar.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'south',
    'userena',
    'guardian',
    'easy_thumbnails',
    # my_apps
    'upload',
)

INTERNAL_IPS = ('127.0.0.1',)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
USERENA_WITHOUT_USERNAMES = True
USERENA_ACTIVATION_REQUIRED=False
USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_DEFAULT_PRIVACY = 'closed'

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE='upload.BlackbarProfile'

