from django.contrib import admin

from .models import Bem, Divida, Endereco, Pessoa


admin.site.register([Bem, Divida, Endereco, Pessoa])
