from django.shortcuts import render
# Create your views here.

def principal(request):
    alumnos = 0
    return render(request, "inicio/principal.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")