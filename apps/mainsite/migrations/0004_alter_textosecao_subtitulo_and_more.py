# Generated by Django 5.1.1 on 2024-10-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_textosecao_imagemsecao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textosecao',
            name='subtitulo',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='textosecao',
            name='texto_botao',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='textosecao',
            name='titulo',
            field=models.CharField(max_length=350),
        ),
    ]
