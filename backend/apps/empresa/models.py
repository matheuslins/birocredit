from django.db import models


class Biro(models.Model):
    nome = models.CharField('Bereau', max_length=100)
    site = models.CharField('Site', max_length=100)

    def __str__(self):
        return str(self.nome or "[Not set]")

    class Meta:
        verbose_name = 'Bereau'
        verbose_name_plural = 'Bereaus'


class Empresa(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.IntegerField('Status')

    def __str__(self):
        return str(self.razao_social or "[Not set]")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
