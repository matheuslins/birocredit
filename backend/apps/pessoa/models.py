from django.db import models

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
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Empresa(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.IntegerField('Status')

    def __str__(self):
        return str(self.razao_social or "[Not set]")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Divida(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="divida_empresa",
        verbose_name='empresa'
    )
    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_DIVIDA)
    status = models.CharField('Status', max_length=1, choices=STATUS_DIVIDA)
    valor = models.IntegerField('valor')
    juro = models.IntegerField('Juro Acumulado')

    def __str__(self):
        return str(
            str(self.tipo or "[Not set]") + str(self.status or "[Not set]"))

    class Meta:
        verbose_name = 'Divida'
        verbose_name_plural = 'Dividas'


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF')
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
