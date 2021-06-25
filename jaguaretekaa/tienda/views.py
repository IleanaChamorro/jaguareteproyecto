from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    sesion = request.session
    return render(request, 'templates/index.html', {
        'sesion': sesion
    })


def about(request):
    pass
