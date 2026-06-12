from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html",{"productos":productos})
    
def borrar_producto(request):
    producto = Producto.objects.get(id=id)
    producto.delete()

def actualizar_producto(request):
    pass

def crear_producto(request):
    pass