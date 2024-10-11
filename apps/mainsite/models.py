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


class Ferramenta(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name="descrição", max_length=100)
    imagem = models.ImageField(upload_to="fotos/ferramentas/")

    # TODO: definir como melhor tratar a URL de direcionamento
    url = models.URLField(
        verbose_name="link de direcionamento",
        default="#",
        help_text="http://www.exemplo.com/ferramenta-site",
    )

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    qualificacao = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to="fotos/equipe/")

    # Esse campo foi inserido pensando em preparar o sistema para uma futura implementação de páginas para cada membro
    biografia = models.TextField(verbose_name="breve biografia", max_length=300)

    def __str__(self):
        return self.nome


class CategoriaApoio(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="fotos/categorias_apoio/")

    # TODO: definir qual formato de URL será utilizado
    @property
    def url(self):
        "Retorna uma url que substitui espaços por hífens no campo nome."
        return self.nome.replace(" ", "-")

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    conteudo = models.TextField(verbose_name="conteúdo")
    thumbnail = models.ImageField(upload_to="artigos/thumbnails/")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
