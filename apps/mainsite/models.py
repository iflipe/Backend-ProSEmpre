from django.db import models
from django.core.validators import RegexValidator


class CategoriaVideo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(verbose_name="breve descrição", max_length=120)
    icone = models.ImageField(upload_to="icones/categorias/")

    def __str__(self):
        return self.nome


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        CategoriaVideo, on_delete=models.SET_NULL, to_field="nome", null=True
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


class SubCategoriaApoio(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="fotos/cards/")
    categoria = models.ForeignKey(CategoriaApoio, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class ArtigoBlog(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    conteudo = models.TextField(verbose_name="conteúdo")
    thumbnail = models.ImageField(upload_to="artigos/thumbnails/")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class RecursoApoio(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.ForeignKey(SubCategoriaApoio, on_delete=models.CASCADE)
    conteudo = models.FileField(upload_to="recursos/")
    thumbnail = models.ImageField(upload_to="recursos/thumbnails/")

    def __str__(self):
        return self.nome


class Contato(models.Model):
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r"^\+?\d{0,3}\s?\(?\d{0,2}\)?\s?[\d\-\s]{9,15}$")],
    )
    email = models.EmailField()
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.telefone + " / " + self.email


class RedesSociais(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    icone = models.ImageField(upload_to="icones/redes_sociais/")
    url = models.URLField()

    def __str__(self):
        return self.url


class TextoSecao(models.Model):
    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    subtitulo = models.TextField(max_length=150)
    url = models.CharField(max_length=50)
    texto_botao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class ImagemSecao(models.Model):
    conteudo = models.ImageField(upload_to="fotos/secoes/")
    secao = models.ForeignKey(TextoSecao, on_delete=models.CASCADE)

    def __str__(self):
        return self.secao
