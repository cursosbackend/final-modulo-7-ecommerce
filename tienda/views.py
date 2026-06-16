from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForms
from django.contrib import messages

# Create your views here.
#crud
#c (create)
def crear_producto(request):
    #si el usuario envio el formulario 
    if request.method == "POST":
        form = ProductoForms(request.POST, request.FILES) #request.POST (SON TODOS LOS DATOS DEL FORMULARIO)
        if form.is_valid():
            form.save()
            messages.success(request, "producto guardado correctamente")
            return redirect("lista_productos")
    else:
        form = ProductoForms()

    return render(request, "crear_producto.html",{"form":form})
#crud
# r (lectura de datos)   

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html",{"productos":productos})



def borrar_producto(request):
    producto = Producto.objects.get(id=id)
    producto.delete()

def actualizar_producto(request):
    pass

