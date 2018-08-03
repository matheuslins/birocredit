from .common import *

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS',
    default=['www.yourdomain.com'])

DEBUG = env.bool('DEBUG')

DATABASES.update({
    'postgresdb_1': env.db('DB1_URL'),  # BASE 1
    'postgresdb_2': env.db('DB2_URL'),  # BASE 2
    'mongogb': env.db('DB3_URL'),  # BASE 3
})

DATABASES['postgresdb_1']['ATOMIC_REQUESTS'] = True
DATABASES['postgresdb_2']['ATOMIC_REQUESTS'] = True
DATABASES['mongogb']['ATOMIC_REQUESTS'] = True
