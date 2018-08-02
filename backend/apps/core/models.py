from django.db import models


class Evento(models.Model):
    pass


class Empresa(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.IntegerField('Status')

    def __str__(self):
        return str(self.razao_social or "[Not set]")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
