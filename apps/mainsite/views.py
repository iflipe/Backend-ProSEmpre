from django.shortcuts import render
from .utils import get_footer
from .models import (
    CategoriaApoio,
    TextoSecao,
    ImagemSecao,
    CategoriaVideo,
    Ferramenta,
    Equipe,
    ArtigoBlog,
)
import random


def pais_e_profs(request):
    # Busca a seção de texto para exibição
    secao_pais_e_profs = TextoSecao.objects.filter(nome="hero-pais-e-profs").first()
    categorias = CategoriaApoio.objects.all()

    # Busca até 9 subcategorias de recursos para exibir aleatoriamente por categoria
    pag_aleatoria_por_categoria = {}
    for categoria in categorias:
        paginas_por_categoria = categoria.paginas.all()

        paginas_aleatorias = random.sample(
            list(paginas_por_categoria), min(9, len(paginas_por_categoria))
        )
        pag_aleatoria_por_categoria[categoria.nome] = {
            "categoria": categoria,
            "paginas": paginas_aleatorias,
        }

    context = {
        "secao": secao_pais_e_profs,
        "categoria_paginas": pag_aleatoria_por_categoria,
    }
    context.update(get_footer())

    return render(request, "pais-e-profs.html", context)


def videos(request):
    # Busca a seção de texto para exibição
    secao = TextoSecao.objects.filter(nome="hero-videos").first()
    imagens_hero = ImagemSecao.objects.filter(secao=secao).all()[:7]
    categorias = CategoriaVideo.objects.all()

    # Busca até 9 vídeos aleatórios por categoria para exibir
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
        "imagens": [],  # Inicializa a lista vazia
    }
    context.update(get_footer())

    # Verifica o tamanho da lista resultado e adiciona as imagens
    if len(imagens_hero) > 0:
        context["imagens"].append(
            {"imagem": imagens_hero[0], "tamanho": "Pequeno", "dupla": False}
        )
    if len(imagens_hero) > 1:
        context["imagens"].append(
            {"imagem": imagens_hero[1:3], "tamanho": "Pequeno", "dupla": True}
        )
    if len(imagens_hero) > 3:
        context["imagens"].append(
            {"imagem": imagens_hero[3], "tamanho": "Grande", "dupla": False}
        )
    if len(imagens_hero) > 4:
        context["imagens"].append(
            {"imagem": imagens_hero[4:6], "tamanho": "Pequeno", "dupla": True}
        )
    if len(imagens_hero) > 6:
        context["imagens"].append(
            {"imagem": imagens_hero[6], "tamanho": "Pequeno", "dupla": False}
        )

    return render(request, "videos.html", context)


def home(request):

    # Busca um único resultado para as seções do site
    secao_home = TextoSecao.objects.filter(nome="hero-home").first()
    secao_equipe = TextoSecao.objects.filter(nome="equipe").first()
    secao_blog = TextoSecao.objects.filter(nome="blog").first()
    secao_apoio = TextoSecao.objects.filter(nome="pais-e-profs").first()

    # Já que as seções de vídeos e jogos são coloridas, as exibimos de forma aleatória
    secao_colorida = (
        TextoSecao.objects.filter(nome="videoshome").values()
        | TextoSecao.objects.filter(nome="jogoshome").values()
    )
    secao_aleatoria = random.sample(list(secao_colorida), min(2, len(secao_colorida)))

    ferramentas = Ferramenta.objects.all()
    categorias = CategoriaApoio.objects.all()
    equipe = Equipe.objects.all()

    # Seleciona da lista completa de artigos até 3 aleatoriamente para exibir na home
    artigos_lista = ArtigoBlog.objects.all()
    artigos = random.sample(list(artigos_lista), min(3, len(artigos_lista)))

    context = {
        "secao_home": secao_home,
        "secao_equipe": secao_equipe,
        "secao_blog": secao_blog,
        "secao_apoio": secao_apoio,
        "ferramentas": ferramentas,
        "equipe": equipe,
        "artigos": artigos,
        "secao_cores": secao_aleatoria,
        "categorias": categorias,
    }
    context.update(get_footer())

    return render(request, "home.html", context)
