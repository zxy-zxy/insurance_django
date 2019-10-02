from .base import *

ALLOWED_HOSTS = ['0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance_dev',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'insurance-db',
        'PORT': 5432,
    }
}