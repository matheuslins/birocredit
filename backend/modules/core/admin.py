from django.contrib import admin

from .models import Compra, Consulta, Evento, Movimentacao


admin.site.register([Consulta, Movimentacao, Compra, Evento])
