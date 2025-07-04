from django.contrib import admin
from .models import *
# Register your models here.


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    
admin.site.register(Alumnos, AdministrarModelo)

class AdminComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
admin.site.register(Comentarios, AdminComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
    