from .settings import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'tra_db',
#         'USER': 'postgres',
#         'PASSWORD': '1040',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-f%v$&$h70+&ful*6dd=@$o=44e*dt=hcgs+)f-1u3#8#@)2@1)'
