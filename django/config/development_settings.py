from .common_settings import *

DEBUG = True

SECRET_KEY = 'secret key'

DATABASES['default']['NAME'] = 'mailape'
DATABASES['default']['USER'] = 'mailape'
DATABASES['default']['PASSWORD'] = 'development'
DATABASES['default']['HOST'] = 'localhost'
DATABASES['default']['PORT'] = '5432'

MAILING_LIST_FROM_EMAIL = 'mailape@example.com'
MAILING_LIST_LINK_DOMAIN = 'http://localhost'

EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'username'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CELERY_BROKER_URL = 'redis://localhost:6379/0'

