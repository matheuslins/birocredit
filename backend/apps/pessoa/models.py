from django.db import models

from birocredit.utils import parser_choice
from empresa import models as empresa_models
from .constants import TIPOS_DIVIDA, STATUS_DIVIDA


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=100)
    numero = models.IntegerField('Numero')
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cep = models.CharField('CEP', max_length=100)

    def __str__(self):
        return str(self.rua or "[Not set]")

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', unique=True, max_length=14)
    idade = models.IntegerField('Idade', null=True, blank=True)
    fonte_renda = models.TextField(
        null=True, blank=True, verbose_name='fonte_renda')
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        related_name="pessoa_endereco",
        verbose_name='endereco'
    )

    def __str__(self):
        return str(self.nome or "[Not set]")

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        unique_together = (("nome", "cpf"),)


class Bem(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="bem_pessoa",
        verbose_name='pessoa'
    )
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
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="divida_pessoa",
        verbose_name='pessoa'
    )
    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_DIVIDA)
    status = models.CharField('Status', max_length=1, choices=STATUS_DIVIDA)
    valor = models.FloatField('Valor', null=True, blank=True)
    juro = models.IntegerField('Juro Acumulado', null=True, blank=True)

    def __str__(self):
        return " -> ".join([
            str(parser_choice(self.tipo, TIPOS_DIVIDA) or "[Not set]"),
            str(parser_choice(self.status, STATUS_DIVIDA) or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Divida'
        verbose_name_plural = 'Dividas'
