# Generated by Django 5.1.7 on 2025-03-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Data de Falecimento')),
                ('nationality', models.CharField(max_length=100, verbose_name='Nacionalidade')),
                ('biography', models.TextField(blank=True, verbose_name='Biografia')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Altura (m)')),
                ('social_media', models.JSONField(blank=True, null=True, verbose_name='Redes Sociais')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
                'ordering': ['name'],
            },
        ),
    ]
