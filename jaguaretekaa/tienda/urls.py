from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('acceder/', views.acceder, name="acceder"),
]
