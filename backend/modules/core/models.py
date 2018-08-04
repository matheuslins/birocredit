from django.db import models
from django.contrib.postgres.fields import ArrayField

from birocredit.utils import parser_choice
from empresa import models as empresa_models
from pessoa import models as pessoa_models
from .constants import TIPOS_MOVIMENTACAO


class Consulta(models.Model):
    biro = models.ForeignKey(
        empresa_models.Biro,
        on_delete=models.CASCADE,
        related_name="consulta_biro",
        verbose_name='biro'
    )
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " -> ".join([
            str(self.data or "[Not set]"),
            str(self.biro.nome or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


class Movimentacao(models.Model):
    choices = TIPOS_MOVIMENTACAO
    pessoa = models.ForeignKey(
        pessoa_models.Pessoa,
        on_delete=models.CASCADE,
        related_name="movimentacao_pessoa",
        verbose_name='pessoa'
    )
    tipo = models.CharField('Tipo', max_length=1, choices=choices)
    valor = models.FloatField('Valor')

    def __str__(self):
        return " -> ".join([
            str(self.pessoa.nome or "[Not set]"),
            str(parser_choice(self.tipo, self.choices) or "[Not set]"),
            str(self.valor or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Movimentacao'
        verbose_name_plural = 'Movimentacoes'


class Compra(models.Model):
    pessoa = models.ForeignKey(
        pessoa_models.Pessoa,
        on_delete=models.CASCADE,
        related_name="compra_pessoa",
        verbose_name='pessoa'
    )
    itens = ArrayField(models.CharField('Item', max_length=100))
    valor = models.FloatField('Valor')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " -> ".join([
            str(self.pessoa.nome or "[Not set]"),
            str(self.valor or "[Not set]"),
        ])

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Evento(models.Model):
    pessoa = models.ForeignKey(
        pessoa_models.Pessoa,
        on_delete=models.CASCADE,
        related_name="evento_pessoa",
        verbose_name='pessoa'
    )
    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name="evento_consulta",
        verbose_name='consulta'
    )

    def __str__(self):
        return "->".join([
            str(self.pessoa.nome or "[Not set]"),
            str(self.consulta.biro.nome or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
