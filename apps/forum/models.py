from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    foto_perfil = models.ImageField(upload_to="fotos/usuarios/", blank=True, null=True)

    def __str__(self):
        return self.nome


class TopicoForum(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.nome + ": " + self.titulo


class ComentarioTopico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    topico = models.ForeignKey(TopicoForum, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
