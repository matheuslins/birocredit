from .common import *

SECRET_KEY = env('SECRET_KEY_LOCAL')

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS_LOCAL',
    default=['www.yourdomain.com'])

DEBUG = env.bool('DEBUG_LOCAL')

DATABASES = {
    'default': env.db('DB1_URL_LOCAL'),  # BASE 1
    'db_2': env.db('DB2_URL_LOCAL'),  # BASE 2
    # 'db_3': env.db('DB3_URL_LOCAL'),  # BASE 3
}
