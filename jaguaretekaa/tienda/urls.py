from django.urls import include, path

from . import views

app_name = "tienda"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('acceder/', views.acceder, name="acceder"),
]
