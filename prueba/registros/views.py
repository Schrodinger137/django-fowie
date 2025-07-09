from django.shortcuts import render, redirect
from .models import *
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
# Create your views here.

def registros(request):
    alumnos = Alumnos.objects.all()
    
    return render(request, 'registros/principal.html', {
        'alumnos':alumnos
        })
    
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comentarios')
    
    form = ComentarioContactoForm()

    return render(request, 'registros/contacto.html', {
        'form':form
    }) 

def contacto(request):
    return render(request,"registros/contacto.html")

def comentarios(request):
    comentarios = ComentarioContacto.objects.all()
    
    return render(request, 'registros/listaComentarios.html', {
        'comentarios':comentarios
    })

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/contacto.html', {
            'comentarios':comentarios
        })
    
    return render(request, confirmacion, {'object':comentario})