import os

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
