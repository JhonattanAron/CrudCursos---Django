from django.shortcuts import render , redirect
# Create your views here.

cursos = [
    {'codigo': 'C001', 'nombre': 'Desarrollo en Python', 'credito': '3'},
    {'codigo': 'C002', 'nombre': 'Desarrollo en Java', 'credito': '4'},
    {'codigo': 'C003', 'nombre': 'Desarrollo en Angular', 'credito': '2'},
    {'codigo': 'C004', 'nombre': 'Frontend con React', 'credito': '3'},
    {'codigo': 'C005', 'nombre': 'Backend con Spring Boot', 'credito': '5'},
] 

def home(request):
    return render(request, "gestionCursos.html", {"cursos": cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['txtCreditos']

    curso = {
        'codigo': codigo,
        'nombre': nombre,
        'credito': credito
    }

    cursos.append(curso)

    return redirect('/')

def eliminarCurso(request, codigo):
    curso_index = None
    for index, curso in enumerate(cursos):
        if curso['codigo'] == codigo:
            curso_index = index
            break

    if curso_index is not None:
        cursos.pop(curso_index)

    return redirect('/')

def editarCurso(request, codigo):
    curso = None
    for c in cursos:
        if c['codigo'] == codigo:
            curso = c
            break

    return render(request, "gestionCursos.html", {"editarCurso": curso})

def edicionCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['txtCreditos']

    for curso in cursos:
        if curso['codigo'] == codigo:
            curso['nombre'] = nombre
            curso['credito'] = credito
            break

    return redirect('/')
