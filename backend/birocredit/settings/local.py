from .common import *

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS',
    default=['www.yourdomain.com'])

DEBUG = env.bool('DEBUG')

# TODO: Trabalhar com multiplos databases
DATABASES = {
    'default': env.db('DATABASE_URL'),  # BASE 1
    # 'postgresdb_2': env.db('DB2_URL'),  # BASE 2
    # 'mongogb': env.db('DB3_URL'),  # BASE 3 # TODO: Criar um Middleware para lidar com o mongo
)
DATABASES['default']['ATOMIC_REQUESTS'] = True
