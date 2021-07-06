from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm

from .models import Producto


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'):
            self.fields[field].widget.attrs = {'class': 'form-control'}
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password1', 'password2']

class NuevoProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=[
            'titulo','categoria','descripcion','precio','imagen'
        ]
