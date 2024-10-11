from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(verbose_name="breve descrição", max_length=120)
    icone = models.ImageField(upload_to="icones/categorias/")

    def __str__(self):
        return self.nome


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, to_field="nome", null=True
    )
    conteudo = models.FileField(upload_to="videos/")
    thumbnail = models.ImageField(upload_to="videos/thumbnails/")
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
