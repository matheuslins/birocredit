from django.contrib import admin

from .models import Empresa, Biro


admin.site.register([Empresa, Biro])
