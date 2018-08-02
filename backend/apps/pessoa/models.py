from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        unique_together = (("nome", "cpf"),)
