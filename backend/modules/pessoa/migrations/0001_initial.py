# Generated by Django 2.1 on 2018-08-04 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '__first__'),
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
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('biro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta_biro', to='empresa.Biro', verbose_name='biro')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Divida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('C', 'Cartão de Crédito'), ('T', 'Telefonia'), ('E', 'Energia'), ('U', 'IPTU'), ('A', 'IPVA')], max_length=1, verbose_name='Tipo')),
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
                ('cep', models.CharField(max_length=100, verbose_name='CEP')),
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
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Idade')),
                ('fonte_renda', models.TextField(blank=True, null=True, verbose_name='fonte_renda')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_endereco', to='pessoa.Endereco', verbose_name='endereco')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AddField(
            model_name='divida',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divida_pessoa', to='pessoa.Pessoa', verbose_name='pessoa'),
        ),
        migrations.AddField(
            model_name='bem',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bem_pessoa', to='pessoa.Pessoa', verbose_name='pessoa'),
        ),
        migrations.AlterUniqueTogether(
            name='pessoa',
            unique_together={('nome', 'cpf')},
        ),
    ]