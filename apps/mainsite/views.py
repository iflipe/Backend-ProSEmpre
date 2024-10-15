from django.shortcuts import render
from .models import (
    CategoriaApoio,
    TextoSecao,
    ImagemSecao,
    CategoriaVideo,
    Ferramenta,
    Equipe,
    ArtigoBlog,
    RecursoApoio,
    Contato,
    RedesSociais,
)
import random

def pais_e_profs(request):
    secao_pais_e_profs = TextoSecao.objects.filter(nome="hero-pais-e-profs").first()
    categorias = CategoriaApoio.objects.all()

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

    contato = Contato.objects.first()
    redes_sociais = RedesSociais.objects.all()

    context = {
        "secao": secao_pais_e_profs,
        "categoria_paginas": pag_aleatoria_por_categoria,
        "contato": contato,
        "redes_sociais": redes_sociais,}

    return render(request, "pais-e-profs.html", context)

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

    contato = Contato.objects.first()
    redes_sociais = RedesSociais.objects.all()
    
    context = {
        "secao": secao,
        "categorias_videos": videos_aleatorios_por_categoria,
        "imagens": [],  # Inicializa a lista vazia
        "contato": contato,
        "redes_sociais": redes_sociais,
    }

    # Verifica o tamanho da lista resultado e adiciona as imagens
    if len(resultado) > 0:
        context["imagens"].append({"imagem": resultado[0], "tamanho": "Pequeno", "dupla": False})
    if len(resultado) > 1:
        context["imagens"].append({"imagem": resultado[1:3], "tamanho": "Pequeno", "dupla": True})
    if len(resultado) > 3:
        context["imagens"].append({"imagem": resultado[3], "tamanho": "Grande", "dupla": False})
    if len(resultado) > 4:
        context["imagens"].append({"imagem": resultado[4:6], "tamanho": "Pequeno", "dupla": True})
    if len(resultado) > 6:
        context["imagens"].append({"imagem": resultado[6], "tamanho": "Pequeno", "dupla": False})

    return render(request, "videos.html", context)


def home(request):

    # Busca um único resultado para as seções do site
    secao_home = TextoSecao.objects.filter(nome="herohome").first()
    secao_equipe = TextoSecao.objects.filter(nome="equipe").first()
    secao_blog = TextoSecao.objects.filter(nome="blog").first()
    secao_apoio = TextoSecao.objects.filter(nome="pais-e-profs").first()

    # Já que as seções de vídeos e jogos são coloridas, as exibimos de forma aleatória
    secao_colorida = (
        TextoSecao.objects.filter(nome="videoshome").values()
        | TextoSecao.objects.filter(nome="jogoshome").values()
    )
    secao_aleatoria = random.sample(list(secao_colorida), min(2, len(secao_colorida)))

    contato = Contato.objects.first()
    redes_sociais = RedesSociais.objects.all()

    ferramentas = Ferramenta.objects.all()
    categorias = CategoriaApoio.objects.all()
    equipe = Equipe.objects.all()

    # Seleciona da lista completa de artigos 3 aleatoriamente para exibir na home
    artigos_lista = ArtigoBlog.objects.all()
    artigos = random.sample(list(artigos_lista), min(3, len(artigos_lista)))

    context = {
        "secao_home": secao_home,
        "secao_equipe": secao_equipe,
        "secao_blog": secao_blog,
        "secao_apoio": secao_apoio,
        "ferramentas": ferramentas,
        "equipe": equipe,
        "contato": contato,
        "redes_sociais": redes_sociais,
        "artigos": artigos,
        "secao_cores": secao_aleatoria,
        "categorias": categorias,
    }
    return render(request, "home.html", context)

