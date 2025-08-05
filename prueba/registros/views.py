from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages
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

def consultarComentarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)

    return render(request, 'registros/formEditarComentario.html', {
        'comentario':comentario
    })

def editarComentrioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        
        return render(request, 'registros/listaComentarios.html', {
            'comentarios':comentarios
        })
    
    return render(request, 'registros/formEditarComentario.html', {
        'comentario':comentario
        })

def consultas1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })

def consultas2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultas3(request):
    alumnos=Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })

def consultas4(request):
    alumnos=Alumnos.objects.filter(turno__contains='Vesp')
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })

def consultas5(request):
    alumnos = Alumnos.objects.filter(nombre__in=['Juan', 'Ana'])
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })

def consultas6(request):
    fechaInicio = datetime.date(2025, 6, 1)
    fechaFin = datetime.date(2025, 7, 13)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })

def consultas7(request):
    alumnos = Alumnos.objects.filter(comentarios__coment__contains='No inscrito')
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
        })

def consultas8(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 9)
    comentariosContacto = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/listaComentarios.html', {
        'comentariosContacto':comentariosContacto
    })

def consultas9(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__contains='jabua')
    return render(request, 'registros/listaComentarios.html', {
        'comentarios':comentarios
    })

def consultas10(request):
    comentarios = ComentarioContacto.objects.filter(usuario__in=['Fowie'])
    return render(request, 'registros/listaComentarios.html',{
        'comentarios':comentarios
    })

def consultas11(request):
    comentarios = ComentarioContacto.objects.all().only('mensaje')
    return render(request, 'registros/listaComentarios2.html',{
        'comentarios':comentarios
    })

def consultas12(request):
    comentarios = ComentarioContacto.objects.filter(usuario__startswith='Fo')
    return render(request, 'registros/listaComentarios.html', {
        'comentarios':comentarios
    })

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, 'registros/consultas.html', {
        'alumnos':alumnos
    })