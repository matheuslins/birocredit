from django.db import models

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
        return "->".join([
            str(self.id or "[Not set]"),
            str(self.biro.name or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


class Movimentacao(models.Model):
    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_MOVIMENTACAO)
    valor = models.FloatField('Valor')

    def __str__(self):
        return "->".join([
            str(self.tipo or "[Not set]"),
            str(self.valor or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Movimentacao'
        verbose_name_plural = 'Movimentacoes'


class Compra(models.Model):
    item = models.CharField('Item', max_length=100)
    valor = models.FloatField('Valor')
    data = models.DateTimeField(auto_now_add=True)
    parcelado = models.BooleanField('Parcelado?')
    qtd_parcela = models.IntegerField('Quantidade de Parcelas')
    a_vista = models.BooleanField('A vista?')

    def __str__(self):
        return "->".join([
            str(self.item or "[Not set]"),
            str(self.valor or "[Not set]")
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
        verbose_name='biro'
    )
    movimentacao = models.ForeignKey(
        Movimentacao,
        on_delete=models.CASCADE,
        related_name="evento_movimentacao",
        verbose_name='movimentacao'
    )
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="evento_movimentacao",
        verbose_name='movimentacao'
    )

    def __str__(self):
        return "->".join([
            str(self.pessoa.nome or "[Not set]"),
            str(self.movimentacao.tipo or "[Not set]")
        ])

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
