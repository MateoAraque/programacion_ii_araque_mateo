from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

def register(request):
    """Registro de ususarios"""
    return HttpResponse("Registro de Usuarios en líbreria")

def inicio(request):
    """Primer mensaje en mi app"""
    return HttpResponse("Hola estoy programando")

def greeting (request, nombre):
    """Registro de ususarios"""
    return HttpResponse(
        f"Hola {nombre}, bienvenido a TaskFlow"
    )

def destino(request, titulo, nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido {titulo} {nombre}, su cargo es: {cargo}"
    )

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)