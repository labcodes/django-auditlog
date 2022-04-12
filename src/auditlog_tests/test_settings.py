"""
Settings file for the Auditlog test suite.
"""
import os
import django

SECRET_KEY = 'test'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'auditlog',
    'auditlog_tests',
    'multiselectfield',
]

middlewares = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
)

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = middlewares
else:
    MIDDLEWARE = middlewares

if django.VERSION <= (1, 9):
    POSTGRES_DRIVER = 'django.db.backends.postgresql_psycopg2'
else:
    POSTGRES_DRIVER = 'django.db.backends.postgresql'

DATABASE_ROUTERS = ['auditlog_tests.router.PostgresRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'auditlog_tests.db',
    },
    'postgres': {
        'ENGINE': POSTGRES_DRIVER,
        'NAME': 'auditlog_tests_db',
        'USER': 'splendidspoon',
        'PASSWORD': 'dev1',
        'HOST': '127.0.0.1',
        'PORT': '5454',
    }
}

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]
if django.VERSION[:2] >= (3, 2):
    TEMPLATES[0]['OPTIONS']['context_processors'] = [
        'django.template.context_processors.request',
        *TEMPLATES[0]['OPTIONS']['context_processors']
    ]

ROOT_URLCONF = 'auditlog_tests.urls'

USE_TZ = True
