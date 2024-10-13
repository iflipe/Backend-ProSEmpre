from django.contrib import admin
from .models import Usuario, TopicoForum, ComentarioTopico

admin.site.register(Usuario)
admin.site.register(TopicoForum)
admin.site.register(ComentarioTopico)
