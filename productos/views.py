from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all().values()
    return render(
        request,
        'index.html', 
        {'productos': productos})
