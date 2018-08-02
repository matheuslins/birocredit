from django.db import models

from apps.pessoa.models import Pessoa
from .constants import TIPOS_MOVIMENTACAO


class Biro(models.Model):
    nome = models.CharField('Bereau', max_length=100)
    site = models.CharField('Site', max_length=100)

    def __str__(self):
        return str(self.nome or "[Not set]")

    class Meta:
        verbose_name = 'Bereau'
        verbose_name_plural = 'Bereaus'


class Consulta(models.Model):
    biro = models.ForeignKey(
        Biro,
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
        Pessoa,
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


class Empresa(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.IntegerField('Status')

    def __str__(self):
        return str(self.razao_social or "[Not set]")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
