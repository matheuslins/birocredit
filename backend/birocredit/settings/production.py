from .common import *

SECRET_KEY = env('SECRET_KEY_PROD')

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS_PROD',
    default=['www.yourdomain.com'])

DEBUG = env.bool('DEBUG_PROD')

DATABASES = {
    'default': env.db('DB1_URL_PROD'),  # BASE 1
    'db_2': env.db('DB2_URL_PROD'),  # BASE 2
    'db_3': env.db('DB3_URL_PROD'),  # BASE 3
}
