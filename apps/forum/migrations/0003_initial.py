# Generated by Django 5.1.1 on 2024-10-16 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum', '0002_remove_topicoforum_usuario_remove_usuario_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos/usuarios/')),
            ],
        ),
        migrations.CreateModel(
            name='TopicoForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('conteudo', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioTopico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topicoforum')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.usuario')),
            ],
        ),
    ]
