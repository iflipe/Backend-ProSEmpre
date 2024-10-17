from .models import Contato, RedesSociais, Informacoes


def get_footer():
    return {
        "contato": Contato.objects.first(),
        "redes_sociais": RedesSociais.objects.all(),
        "informacoes": Informacoes.objects.all(),
    }
