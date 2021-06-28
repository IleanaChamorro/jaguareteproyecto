from django.urls import include, path

from . import views

app_name = "tienda"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('footer/', views.footer, name="footer"),
]