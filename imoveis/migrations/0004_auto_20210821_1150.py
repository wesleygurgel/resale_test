# Generated by Django 3.2.6 on 2021-08-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_alter_imovel_imobiliaria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imobiliaria',
            options={'ordering': ['id'], 'verbose_name': 'Imobiliaria', 'verbose_name_plural': 'Imobiliarias'},
        ),
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ['id'], 'verbose_name': 'Imóvel', 'verbose_name_plural': 'Imóveis'},
        ),
        migrations.AlterField(
            model_name='imobiliaria',
            name='endereco',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='imobiliaria',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='descricao',
            field=models.TextField(default='Digite aqui a descrição do Imóvel'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='endereco',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]