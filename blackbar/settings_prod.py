from settings_dev import *

DEBUG = TEMPLATE_DEBUG = False

USERENA_ACTIVATION_REQUIRED=False
USERENA_SIGNIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
    'ENGINE':	'django.db.backends.sqlite3',
	'NAME': 'blackbar.db',
    }
}
