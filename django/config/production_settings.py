from .common_settings import *

DEBUG = False

assert SECRET_KEY is not None, (
    'Please provide DJANGO_SECRET_KEY environment variable with a value')

ALLOWED_HOSTS += [
    os.getenv('DJANGO_ALLOWED_HOSTS'),
]

DATABASES['default'].update({
    'NAME': os.getenv('DJANGO_DB_NAME'),
    'USER': os.getenv('DJANGO_DB_USER'),
    'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
    'HOST': os.getenv('DJANGO_DB_HOST'),
    'PORT': os.getenv('DJANGO_DB_PORT'),
})

LOGGING['handlers']['main'] = {
    'class': 'logging.handlers.WatchedFileHandler',
    'level': 'DEBUG',
    'filename': os.getenv('DJANGO_LOG_FILE')
}

MAILING_LIST_FROM_EMAIL = os.getenv('MAIL_APE_FROM_EMAIL')
MAILING_LIST_LINK_DOMAIN = os.getenv('DJANGO_ALLOWED_HOSTS')

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_HOST_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_HOST_TLS', 'false').lower() == 'true'

CELERY_BROKER_URL = 'sqs://'
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-west-2',
    'queue_name_prefix': 'mailape-',
}
