# Generated by Django 3.2.6 on 2021-08-20 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Imobiliaria',
                'verbose_name_plural': 'Imobiliarias',
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('Apartamento', 'Apartamento'), ('Casa', 'Casa')], default='Apartamento', max_length=255)),
                ('finalidade', models.CharField(choices=[('Residencial', 'Residencial'), ('Escritorio', 'Escritorio')], default='Residencial', max_length=255)),
                ('descricao', models.TextField(default='Ainda não foi criada uma descrição para este Imóvel')),
                ('caracteristica', models.TextField(blank=True, default='Características ainda não foram especificadas para este Imóvel!')),
                ('ativo', models.BooleanField(default=True)),
                ('imobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_proprietaria', to='imoveis.imobiliaria')),
            ],
            options={
                'verbose_name': 'Imóvel',
                'verbose_name_plural': 'Imóveis',
                'unique_together': {('nome', 'endereco')},
            },
        ),
    ]
