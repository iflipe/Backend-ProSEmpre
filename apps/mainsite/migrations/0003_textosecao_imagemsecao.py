# Generated by Django 5.1.1 on 2024-10-13 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_contato_redessociais'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextoSecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.TextField(max_length=150)),
                ('url', models.CharField(max_length=50)),
                ('texto_botao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImagemSecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.ImageField(upload_to='fotos/secoes/')),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.textosecao')),
            ],
        ),
    ]
