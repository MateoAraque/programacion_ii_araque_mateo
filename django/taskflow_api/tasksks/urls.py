from django.urls import path
from . import views

app_name = "tasksks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register,name="register"),
    path("inicio", views.inicio,name="inicio"),
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("destino/<str:titulo>/<str:nombre>/<str:cargo>/",
         views.destino, name="destino"),
    path("my-first-template",
         views.my_first_template,
         name="my-first-template"),
     path("leads-like",
         views.leads_like,
         name="leads-like")
]

