from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.mainsite.models import TextoSecao, ImagemSecao
from apps.mainsite.utils import get_footer
from .models import TopicoForum, Usuario, ComentarioTopico
import random


def forum(request):
    # Organizacao do hero
    secao = TextoSecao.objects.get(nome="hero-forum")
    imagens_hero = ImagemSecao.objects.filter(secao=secao).all()

    # Organizacao dos topicos
    topicos = TopicoForum.objects.all().order_by("-data_criacao")
    comentarios_topicos = []
    for topico in topicos:
        comentaristas = (
            ComentarioTopico.objects.filter(topico=topico).values("usuario").distinct()
        )
        num_comentaristas = comentaristas.count()

        if num_comentaristas == 0:
            comentarios_topicos.append(
                "Seja o primeiro a comentar em <b>" + topico.titulo + "</b>"
            )
        elif num_comentaristas < 3:
            comentarios_topicos.append(
                "Participe da discussão em <b>" + topico.titulo + "</b>"
            )
        else:
            pessoas = random.sample(list(comentaristas), 2)
            comentarios_topicos.append(
                "Faça como "
                + Usuario.objects.get(pk=pessoas[0]["usuario"]).nome
                + " e "
                + Usuario.objects.get(pk=pessoas[1]["usuario"]).nome
                + " e comente sobre <b>"
                + topico.titulo
                + "</b>"
            )

    # Paginacao dos topicos
    topicos_e_comentarios = list(zip(topicos, comentarios_topicos))
    paginator = Paginator(topicos_e_comentarios, 4)
    page = request.GET.get("page")
    try:
        topicos_e_comentarios = paginator.page(page)
    except PageNotAnInteger:
        topicos_e_comentarios = paginator.page(1)
    except EmptyPage:
        topicos_e_comentarios = paginator.page(paginator.num_pages)

    # Organizacao da secao de topicos populares
    topicos_populares = (
        ComentarioTopico.objects.values("topico")
        .annotate(total_comentarios=Count("*"))
        .order_by("-total_comentarios")[:3]
    )

    for topico in topicos_populares:
        topico["topico"] = TopicoForum.objects.get(pk=topico["topico"])
        topico["comentaristas"] = (
            ComentarioTopico.objects.filter(topico=topico["topico"])
            .values("usuario")
            .distinct()
            .count()
        )

    context = {
        "secao": secao,
        "imagens_hero": imagens_hero,
        "topicos": topicos_e_comentarios,
        "topicos_populares": topicos_populares,
    }
    context.update(get_footer())

    return render(request, "forum.html", context)


def adicionar_topico(request):
    if request.method == "POST":
        texto = request.POST.get("novo_topico")
        usuario = random.sample(list(Usuario.objects.all()), 1)[0]

        # Já que não há campo para título do tópico, vamos considerar que a primeira linha do texto é o título
        if texto:
            titulo = texto.splitlines()[0][:150]
            TopicoForum.objects.create(
                titulo=titulo,
                conteudo=texto,
                usuario=usuario,
            )

    return forum(request)
