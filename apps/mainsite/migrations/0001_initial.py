# Generated by Django 5.1.1 on 2024-10-12 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaApoio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='fotos/categorias_apoio/')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(max_length=120, verbose_name='breve descrição')),
                ('icone', models.ImageField(upload_to='icones/categorias/')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('qualificacao', models.CharField(max_length=50)),
                ('foto_perfil', models.ImageField(upload_to='fotos/equipe/')),
                ('biografia', models.TextField(max_length=300, verbose_name='breve biografia')),
            ],
        ),
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=100, verbose_name='descrição')),
                ('imagem', models.ImageField(upload_to='fotos/ferramentas/')),
                ('url', models.URLField(default='#', help_text='http://www.exemplo.com/ferramenta-site', verbose_name='link de direcionamento')),
            ],
        ),
        migrations.CreateModel(
            name='ArtigoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('conteudo', models.TextField(verbose_name='conteúdo')),
                ('thumbnail', models.ImageField(upload_to='artigos/thumbnails/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoriaApoio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='fotos/cards/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.categoriaapoio')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoApoio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('conteudo', models.FileField(upload_to='recursos/')),
                ('thumbnail', models.ImageField(upload_to='recursos/thumbnails/')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.subcategoriaapoio')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.FileField(upload_to='videos/')),
                ('thumbnail', models.ImageField(upload_to='videos/thumbnails/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.categoriavideo', to_field='nome')),
            ],
        ),
    ]
