from django.contrib import admin

# Register your models here.
from .models import Project, Cementerio


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)   

@admin.register(Cementerio)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre","parcela","created_at")
    search_fields = ("nombre",) 