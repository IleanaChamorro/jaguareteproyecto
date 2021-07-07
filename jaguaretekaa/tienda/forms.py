 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class ProductoForm(forms.ModelForm):

    class Meta:
        model = models.Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
