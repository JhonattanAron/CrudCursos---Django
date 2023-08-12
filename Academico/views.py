from django.shortcuts import render , redirect
from .models import Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    return render(request,"gestionCursos.html" , {"cursos":cursos})

def registrarCurso(request):
    codigo= request.POST['txtCodigo']
    nombre= request.POST['txtNombre']
    credito= request.POST['txtCreditos']

    curso = Curso.objects.create(
        codigo = codigo,
        nombre = nombre,
        credito = credito
    )

    return redirect('/')

def eliminarCurso(request , codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()

    return redirect('/')

def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request , "gestionCursos.html" , {"editarCurso":curso})

def edicionCurso(request):
    codigo= request.POST['txtCodigo']
    nombre= request.POST['txtNombre']
    credito= request.POST['txtCreditos']

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.credito = credito
    curso.save()

    return redirect('/')
