from django.db import models
from django.contrib.postgres.fields import ArrayField

from empresa import models as empresa_models
from .constants import TIPOS_DIVIDA, STATUS_DIVIDA


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=100)
    numero = models.IntegerField('Numero')
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cep = models.IntegerField('CEP')

    def __str__(self):
        return str(self.rua or "[Not set]")

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'


class Bem(models.Model):
    tipo = models.CharField('Tipo', max_length=100)
    valor = models.FloatField('Valor', null=True, blank=True)

    def __str__(self):
        return str(self.tipo or "[Not set]")

    class Meta:
        verbose_name = 'Bem'
        verbose_name_plural = 'Bens'


class Divida(models.Model):
    empresa = models.ForeignKey(
        empresa_models.Empresa,
        on_delete=models.CASCADE,
        related_name="divida_empresa",
        verbose_name='empresa'
    )
    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_DIVIDA)
    status = models.CharField('Status', max_length=1, choices=STATUS_DIVIDA)
    valor = models.FloatField('Valor', null=True, blank=True)
    juro = models.IntegerField('Juro Acumulado', null=True, blank=True)

    def __str__(self):
        return str(
            str(self.tipo or "[Not set]") + str(self.status or "[Not set]"))

    class Meta:
        verbose_name = 'Divida'
        verbose_name_plural = 'Dividas'


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF')
    idade = models.IntegerField('Idade', null=True, blank=True)
    fonte_renda = ArrayField(
        models.TextField(null=True, blank=True, verbose_name='fonte_renda')
    )
    bem = models.ForeignKey(
        Bem,
        on_delete=models.CASCADE,
        related_name="pessoa_bem",
        verbose_name='bem'
    )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        related_name="pessoa_endereco",
        verbose_name='endereco'
    )
    divida = models.ForeignKey(
        Divida,
        on_delete=models.CASCADE,
        related_name="pessoa_divida",
        verbose_name='divida'
    )

    def __str__(self):
        return str(self.nome or "[Not set]")

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        unique_together = (("nome", "cpf"),)
