from settings_dev import *

DEBUG = TEMPLATE_DEBUG = False
DATABASES = {
    'default': {
    'ENGINE':	'django.db.backends.mysql',
	'HOST':		'localhost',
    'NAME': 	'click2eat',
	'USER':		'django_login',
	'PASSWORD':	'*********'
    }
}

INSTALLED_APPS += ('raven.contrib.django',)


SENTRY_SERVERS = ['http://demo.click2eat.ro:9000/store/']
SENTRY_KEY = 'long key'

# Set Sentry's ADMINS to a raw list of email addresses
SENTRY_ADMINS = ('fericean@gmail.com',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
