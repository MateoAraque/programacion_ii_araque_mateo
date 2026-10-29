from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse

from .forms import TaskForm, ProjectForm

from .models import Project, Task

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
    return render(request, "tasksks/my-first-template.html", contexto)

def leads_like(request):
    contexto = {
        "titulo": "ESTUDIANTE",
        "nombre": "Mateo Gabriel",
        "apellido": "Araque Basantes"
    }
    return render(request, "leads/leads-like.html", contexto)

def project_list(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasksks:home")
    else:
        form = TaskForm()

    return render(request, "tasksks/task_form.html", {"form": form, "modo": "crear"})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasksks:home")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasksks/task_form.html", {"form": form, "modo": "editar"})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("tasksks:project-list")
    else:
        form =  ProjectForm()

    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})