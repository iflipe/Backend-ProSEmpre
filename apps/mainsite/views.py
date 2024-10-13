from django.shortcuts import render
from .models import TextoSecao, ImagemSecao, CategoriaVideo, Video
import random


def videos(request):
    secao = TextoSecao.objects.filter(nome="herovideo").first()
    resultado = ImagemSecao.objects.filter(secao=secao).all()[:7]
    categorias = CategoriaVideo.objects.all()

    videos_aleatorios_por_categoria = {}
    for categoria in categorias:
        videos_por_categoria = categoria.videos.all()

        videos_aleatorios = random.sample(
            list(videos_por_categoria), min(9, len(videos_por_categoria))
        )
        videos_aleatorios_por_categoria[categoria.nome] = {
            "categoria": categoria,
            "videos": videos_aleatorios,
        }
    context = {
        "secao": secao,
        "categorias_videos": videos_aleatorios_por_categoria,
        "imagens": [
            {"imagem": resultado[0], "tamanho": "Pequeno", "dupla": False},
            {"imagem": resultado[1:3], "tamanho": "Pequeno", "dupla": True},
            {"imagem": resultado[3], "tamanho": "Grande", "dupla": False},
            {"imagem": resultado[4:6], "tamanho": "Pequeno", "dupla": True},
            {"imagem": resultado[6], "tamanho": "Pequeno", "dupla": False},
        ],
    }

    return render(request, "videos.html", context)
