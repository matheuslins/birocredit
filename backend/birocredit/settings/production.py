from .common import *

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS',
    default=['www.yourdomain.com'])

DEBUG = env.bool('DEBUG')

DATABASES = {
    'default': env.db('DATABASE_URL'),  # BASE 1
    # 'db_2': env.db('DB2_URL'),  # BASE 2
    # 'db_3': env.db('DB3_URL'),  # BASE 3
}

DATABASES['default']['ATOMIC_REQUESTS'] = True
# DATABASES['db_2']['ATOMIC_REQUESTS'] = True
