# Generated by Django 2.1 on 2018-08-03 00:45

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('valor', models.FloatField(blank=True, null=True, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Bem',
                'verbose_name_plural': 'Bens',
            },
        ),
        migrations.CreateModel(
            name='Divida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('C', 'Validação de Campos'), ('T', 'Erro'), ('E', 'Info'), ('U', 'Warning'), ('A', 'Warning')], max_length=1, verbose_name='Tipo')),
                ('status', models.CharField(choices=[('P', 'Paga'), ('N', 'Em aberto')], max_length=1, verbose_name='Status')),
                ('valor', models.FloatField(blank=True, null=True, verbose_name='Valor')),
                ('juro', models.IntegerField(blank=True, null=True, verbose_name='Juro Acumulado')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divida_empresa', to='empresa.Empresa', verbose_name='empresa')),
            ],
            options={
                'verbose_name': 'Divida',
                'verbose_name_plural': 'Dividas',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cep', models.IntegerField(verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Idade')),
                ('fonte_renda', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True, verbose_name='fonte_renda'), size=None)),
                ('bem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_bem', to='pessoa.Bem', verbose_name='bem')),
                ('divida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_divida', to='pessoa.Divida', verbose_name='divida')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_endereco', to='pessoa.Endereco', verbose_name='endereco')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pessoa',
            unique_together={('nome', 'cpf')},
        ),
    ]