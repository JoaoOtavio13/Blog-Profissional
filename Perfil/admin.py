from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.imagem.url))

    image_tag.short_description = 'Image'
    list_display=['nome','idade','email','cpf','data_nascimento','image_tag']

admin.site.register(Instituicao)
admin.site.register(Instrumento)
    