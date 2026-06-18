from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, ProductoPremium
from .forms import ProductoForms, ProductoPremiumForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html",{})


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



#crud 
# u (update)
def actualizar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        form = ProductoForms(request.POST,request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request,"producto actualizado correctamente")
            return redirect("lista_productos")
    else:
        form = ProductoForms(instance=producto)

    return render(request, "actulizar_productos.html",{"form":form})



def borrar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request,"mensaje desde la view!!!!!")
    return redirect("lista_productos")



# crud premium

#create premium
#c (create)
def crear_premium(request):
    # si el request llega por metodo post  pasa algo 
    if request.method == "POST":
        #llega en request con los datos desde en navegador y se cargan en el formulario
        form = ProductoPremiumForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_productos_premium")
    #de lo contrariose entrega el formulario vacio
    else:
        form = ProductoPremiumForms()
    
    return render(request,"premium/formulario_premium.html",{"form":form})

#(lectura de datos)
# read del crud
def lista_productos_premium(request):
    productosPremium = ProductoPremium.objects.all()
    return render(request, "premium/lista_premium.html", {"premium": productosPremium})


def actualizar_premium(requuest):
    pass


def borrar_premium(request):
    pass






    



