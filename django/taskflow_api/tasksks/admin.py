from django.contrib import admin

# Register your models here.
from .models import Project, Cementerio, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)   

@admin.register(Cementerio)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre","parcela","created_at")
    search_fields = ("nombre",) 


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")